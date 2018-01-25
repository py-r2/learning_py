l = ["/","- ","|","\\","|"]
i = 0
while i<30000:
  for item in l:
    print "%s\r" % item,
    i += 1
