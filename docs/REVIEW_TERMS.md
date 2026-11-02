# Shared review term glossary

Use these canonical explanations for both contributors. First-use review explanations are linked below; later reviews should link the relevant entry instead of repeating it. The structured source is [review-terms.json](../curriculum/review-terms.json). Definitions support the existing curriculum; they do not add new mastery concepts or waive independent understanding.

Examples describe each term, not the whole quantity contract: a safe integer can be zero, while an accepted positive quantity must also be greater than zero. Targeted coaching may revisit a term when a learner demonstrates a misunderstanding.

## Positive integer

A whole number greater than zero. It has no fractional part; zero and negative numbers are not positive integers.

Examples:

```js
1
2
3
```

Non-examples:

```js
0
-1
2.5
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/19#discussion_r4434718224).

## Integer

A whole number with no fractional part. Integers may be negative, zero or positive; being an integer alone does not make a value a valid positive quantity.

Examples:

```js
-2
0
3
```

Non-examples:

```js
0.1
2.5
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/19#discussion_r4434718224).

## Safe integer

An integer inside JavaScript Number's reliable integer range, from -9,007,199,254,740,991 through 9,007,199,254,740,991 inclusive. Adjacent integers in this range can be represented and distinguished exactly. This quantity contract additionally requires the integer to be positive.

Examples:

```js
0
3
Number.MAX_SAFE_INTEGER
```

Non-examples:

```js
2.5
Number.MAX_SAFE_INTEGER + 1
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/17#discussion_r4384654134).

## Finite number

A JavaScript number that is neither NaN nor positive or negative Infinity. Finite numbers can have fractional parts, so finiteness alone is not integer validation.

Examples:

```js
0
3
2.5
```

Non-examples:

```js
NaN
Infinity
-Infinity
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/19#discussion_r4434289519).

## Predicate

A function that returns true or false to answer a condition about the input it receives.

Examples:

```js
Number.isInteger(3)
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/19#discussion_r4434718224).

## Argument

A value supplied when calling a function. An omitted argument is undefined unless the function supplies a default; a function does not automatically read a similarly named local value from its caller.

Examples:

```js
Number.isInteger(3) // 3 is the argument supplied to this call
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/19#discussion_r4434718224).

## Truthiness

How JavaScript treats a value in a condition. null acts as false, while an object acts as true.

Examples:

```js
Boolean(null) // false
Boolean({}) // true
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/17#discussion_r4384654121).

## Module export

A value that a file makes available so another file can import and use it.

Examples:

```js
export const featureName = "inventory";
```

[Recorded review explanation](https://github.com/Prem-Tomar/fieldops-mastery/pull/17#discussion_r4384654138).
