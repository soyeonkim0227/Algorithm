h, m = map(int, input().split())
end = int(input())

total = h * 60 + m + end

print('%d %d' % (((total // 60) % 24), total % 60))