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

```javascript
let friendsAtYourParty = 0;

while (friendsAtYourParty < 10) {
    friendsAtYourParty = friendsAtYourParty + 1;
    friendsAtYourParty += 1;
    friendsAtYourParty ++;
    ++friendsAtYourParty;
    // 모두 같은 식 but ++는 뒤에만 쓴다!
    console.log(friendsAtYourParty)
}
```

<br/>

### Incrementing in Loops

```javascript
let friendsAtYourParty = 0;

for (let i = 0; i <=10; i++) {
    friendsAtYourParty++;
}
```

`for ( A ; B ; C) {};`

* A: **the control variable for this particular loop**
  * `i`일 필요는 없지만 다들 항상 `i`를 쓴다
* B: **the control statement**
  * keep doing this until `i` is less than or equal to 10
* C: **run this statement at the end of every loop**
  * 반복이 끝날 때마다 `i`에 1씩 더해나감



<br/>

## Adding Comments

```javascript
// this is some comment to my future self

/* this is

too */
```

<br/>

