from art import logo
print(logo)


def checkHighestBidder(bids):
  highest = 0
  for I in bids:
    if bids[I]>highest:
      highest=bids[I]
      winner = I
  return (winner,highest)

done = True
bids = {}
while (done):
  name = input("What is your name : ")
  bid = int(input("Enter bid amount : "))
  bids[name] = bid
  check = input("Do you want to continue, yes or no? ")
  if check=="yes":
    continue
  else:
    done = False
W = checkHighestBidder(bids)
print("The winner is",W[0],"with a bid of",W[1])

