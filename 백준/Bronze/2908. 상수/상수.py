n1, n2 = map(int, input().split())

def revert(input: int) -> int:
    one = input // 100
    two = (input % 100) // 10
    three = input % 10
    return three*100 + two*10 + one

r1, r2 = revert(n1), revert(n2)
if r1 > r2:
    print(r1)
else:
    print(r2)