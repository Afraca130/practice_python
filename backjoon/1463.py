X = int(input())
cnt = 0


def dp(X, cnt):
    while X != 1:
        if (X % 3) == 0:
            if (X - 1) % 2 == 0:
                cnt += 1
                a = int(dp((X-1), cnt))
                b = int(dp((X/3), cnt))
                # print('a:', a, 'b:', b)
                if a < b:
                    return a
                else:
                    return b
            else:
                cnt += 1
                a = int(dp((X-1), cnt))
                b = int(dp((X/3), cnt))
                # print('a:', a, 'b:', b)
                if a < b:
                    return a
                else:
                    return b

        elif (X % 2) == 0:
            if (X - 1) % 3 == 0:
                cnt += 1
                c = int(dp((X-1), cnt))
                d = int(dp((X/2), cnt))
                # print('c:', c, 'd:', c)
                if c < d:
                    return c
                else:
                    return d
            else:
                cnt += 1
                c = int(dp((X-1), cnt))
                d = int(dp((X/2), cnt))
                # print('c:', c, 'd:', c)
                if c < d:
                    return c
                else:
                    return d

        else:
            X -= 1
            cnt += 1
    return cnt


cnt = dp(X, cnt)

print(cnt)
