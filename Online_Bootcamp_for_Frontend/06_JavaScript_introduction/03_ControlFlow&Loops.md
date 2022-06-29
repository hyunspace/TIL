## Control Flow & Loops

## Control Flow

### if

```javascript
const isSkyBlue = true

if (isSkyBlue) {
  console.log("The sky is blue!")
  console.log("lol")
} else {
  console.log("The sky is... not blue?")
}
```

* block : between `{ }` (curly braces)

* `else` part is not required

```javascript
const isSkyBlue = true

let greeting

if (isSkyBlue) {
  greeting = 'It must be nice weather'
} else {
  greeting = 'It must be bad weather'
}

console.log(greeting)
```

* in this case, can't use `const`

<br/>

## Equality Comparisons

### ===

* just stick with triple equals!

```javascript
if (2 + 2 === 4) {
  console.log('Hooray! Math still works.')
} else {
  console.log('Uh, panic?')
}
>>> true


if (2 + 2 === "4") {
  console.log('Hooray! Math still works.')
} else {
  console.log('Uh, panic?')
}
>>> false
```

<br/>

### ==

```javascript
if (2 + 2 == '4') {
  console.log('Hooray! Math still works.')
} else {
  console.log('Uh, panic?')
}
>>> true
```

<br/>

## If Statement

* Exactly one of these is always going to be executed, unless there's no else.

  ```javascript
  const areTheLightsOn = true
  
  if (areTheLightsOn) {
    // turn the lights off
  } else {
    // turn the lights on
  }
  ```

  * if there's no else and `areTheLightsOn` is false, it just skips and goes on its merry way.

<br/>

## Else If Statement

```javascript
const friendsAtYourParty = 10

if (friendsAtYourParty === 0) {
    console.log('Cool. now I have all the nachos to myself.')
} else if (friendsAtYourParty >= 4) {
    console.log('Perfect amount to play some Kartrider.')
} else {
    console.log('Woooooo, play the dance music!')
}
```

<br/>

<br/>

## Loops

* without loops

  ```javascript
  let friendsAtYourParty = 0
  
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  friendsAtYourParty = friendsAtYourParty + 1
  
  console.log(friendsAtYourParty)
  ```

* `while`

  ```javascript
  let friendsAtYourParty = 0
  
  while (friendsAtYourParty < 10) {
    friendsAtYourParty = friendsAtYourParty + 1
  }
  
  console.log(friendsAtYourParty)
  ```


<br/>

### Incrementing





<br/>

## Adding Comments

```javascript
// this is some comment to my future self

/* this is

too */
```

<br/>

