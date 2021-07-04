import sys


def read_sentence(f):
    prelines = []
    sent = None
    tokens = []
    miscs = []
    while True:
        line = f.readline()
        if line == "":
            assert not sent and not tokens, sent + " " + str(tokens)
            return None, None, None, None
        line = line.rstrip("\n\r")
        if line == "":
            assert sent and tokens
            break
        if line.startswith("#"):
            assert not tokens
            prelines.append(line)
            if line.startswith("# text = "):
                sent = line[9:]
        else:
            assert sent
            r = line.split("\t")
            tokens.append(r[:-1])
            miscs.append({k: v for k, v in (f.split("=", 2) for f in r[-1].split("|"))})
    return prelines, sent, tokens, miscs


with open(sys.argv[1], "r", encoding="utf8") as fold, open(sys.argv[2], "r", encoding="utf8") as fnew:
    while True:
        old_pre, old_sent, old_tokens, old_miscs = read_sentence(fold)
        new_pre, new_sent, new_tokens, new_miscs = read_sentence(fnew)
        if not old_sent:
            assert not new_sent
            break
        if old_sent != new_sent:  # allow skipping only for a sentence
            for line in new_pre:
                print(line, file=sys.stderr)
            for t, m in zip(new_tokens, new_miscs):
                print(*t, "|".join([k + "=" + v for k, v in m.items()]), sep="\t", file=sys.stderr)
            print(file=sys.stderr)
            new_pre, new_sent, new_tokens, new_miscs = read_sentence(fnew)
            assert old_sent == new_sent, ",".join(old_pre) + " != " + ",".join(new_pre)
        ne_spans = []
        ne_type =  None
        ne_begin = None
        offset = 0
        for t, m in zip(old_tokens, old_miscs):
            end = offset + len(t[1])
            if "NE" in m:
                ne  = m["NE"]
                if ne.startswith("B-"):
                    assert not ne_type, ",".join(old_pre) + " != " + ",".join(new_pre)
                    ne_type = ne[2:]
                    ne_begin = offset
                elif ne.startswith("I-"):
                    assert ne_type == ne[2:], ",".join(old_pre) + " != " + ",".join(new_pre)
                elif ne.startswith("L-"):
                    assert ne_type == ne[2:], ",".join(old_pre) + " != " + ",".join(new_pre)
                    ne_spans.append((ne_type, ne_begin, end))
                    ne_type = None
                    ne_begin = None
                elif ne.startswith("U-"):
                    assert not ne_type, ",".join(old_pre) + " != " + ",".join(new_pre)
                    ne_spans.append((ne[2:], offset, end))
                elif ne.startswith("O"):
                    assert not ne_type, ",".join(old_pre) + " != " + ",".join(new_pre)
            if m.get("SpaceAfter", "Yes") == "Yes":
                offset = end + 1
            else:
                offset = end
        assert not ne_type, ",".join(old_pre) + " != " + ",".join(new_pre)

        for line in new_pre:
            print(line)
        ne_index = 0
        offset = 0
        for t, m in zip(new_tokens, new_miscs):
            if ne_index < len(ne_spans):
                ne_type, ne_begin, ne_end = ne_spans[ne_index]
            else:
                ne_type, ne_begin, ne_end = None, len(new_sent), len(new_sent) + 1
            end = offset + len(t[1])
            ne_label = None
            if offset < ne_end and ne_begin < end:
                if offset == ne_begin:
                    if end == ne_end:
                        ne_label = "U-" + ne_type
                        ne_index += 1
                        ne_type = None
                    elif end < ne_end:
                        ne_label = "B-" + ne_type
                    else:
                        assert False, ",".join(old_pre) + " != " + ",".join(new_pre)
                elif end < ne_end:
                    ne_label = "I-" + ne_type
                elif end == ne_end:
                    ne_label = "L" + ne_type
                    ne_index += 1
                    ne_type = None
                else:
                    assert False, ",".join(old_pre) + " != " + ",".join(new_pre)
            if ne_label:
                m["NE"] = ne_label
            print(*t, "|".join([k + "=" + v for k, v in m.items()]), sep="\t")
            if m.get("SpaceAfter", "Yes") == "Yes":
                offset = end + 1
            else:
                offset = end
        assert not ne_type, ",".join(old_pre) + " != " + ",".join(new_pre)
        print()
