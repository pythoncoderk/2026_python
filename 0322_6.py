tag_a, tag_b = input().split()
S = input()

pos = 0

while True:
    start = S.find(tag_a, pos)
    if start == -1:
        break

    content_start = start + len(tag_a)
    end = S.find(tag_b, content_start)

    extracted = S[content_start:end]

    if extracted == "":
        print("<blank>")
    else:
        print(extracted)

    pos = end + len(tag_b)