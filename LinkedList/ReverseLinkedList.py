

curr , prev , nexttemp = head , None , None

while curr:
    nexttemp , curr.next , prev , curr = curr.next , prev , curr , nexttemp

return prev