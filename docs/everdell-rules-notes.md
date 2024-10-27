Change of season: Players start with 2 workers and get more workers at start each season
- +1 in spring
- +1 in summer
- +2 in autumn

Number of cards deealt to players at start
- first player gets 5 cards
- second player gets 6 cards
- third player gets 7 cards
- fourth player gets 8 cards

On your turn, you can:
- Place a Worker
- or Play a Card
- or Prepare for Season



Card Place Fails if:
- It is a unique card and you a;ready have one of that type of card in your city


## Playing 





### Play critter card:

if (the city is full, aka len(city) == 15) {
    return and dont do anything
}

if (the a non-occupied instance of the paired critterCard.construction is present in the players city) {
    play for free (add card to player city)
    mark the construction card as occupied
} else {
    extract the payment (in berries) from the player
}