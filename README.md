# Urban Dictionary Bot  [@UnbanDictionary](https://twitter.com/unbandictionary)

This twitter bot shares fake new definitions based on definitions of newly updated words on Urban Dicitonary.

These new definitions are generated using [markov chains](https://en.wikipedia.org/wiki/Markov_chain).

## Step 1: Get New Words
Use `BeautifulSoup` to scrape the words from the "New" Page on Urban Dictionary.

Pack these words into the `newWords` list

## Step 2: Pick a Random Word
Use `random` to select a random item from `newWords`

## Step 3: Get the Definitions
Use `BeautifulSoup` to scrape the defitions for the randomly selected word.

Append these definitions to `mark`

## Step 4: Generate a New Definition
Use `markovify` library to generate a new definition based on text in `mark`.

New definition is added to `newDef` variable.

`newDef` will return `None` if there isn't enough text in `mark`.

Because of this, Steps 2 - 4 are written into a loop until `newDef` gets a definition.

## Step 5: Tweet New Definition
Use `tweept` to tweet launch the new definition into the dumpster fire known as Twitter.
