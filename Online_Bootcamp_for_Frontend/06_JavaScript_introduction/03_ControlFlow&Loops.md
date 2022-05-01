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

