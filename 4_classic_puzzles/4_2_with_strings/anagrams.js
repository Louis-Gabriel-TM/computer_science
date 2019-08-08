/*
Puzzle Wording
==============
Given two strings, write a function to determine if the second string is an anagram of the first.
Assume that all characters are lowercase letters.
*/

function anagramsWithTwoCounters(s1, s2) {
  if (s1.length !== s2.length) {
    return false;
  }

  let counter1 = {};
  let counter2 = {};
  for (let c of s1) {
    counter1[c] = (counter1[c] || 0) + 1;
  }
  for (let c of s2) {
    counter2[c] = (counter2[c] || 0) + 1;
  }

  for (let key in counter1) {
    if (!(key in counter2)) {
      return false;
    }
    if (counter2[key] !== counter1[key]) {
      return false;
    }
  }

  return true;
}

function anagramsWithOneCounter(s1, s2) {
  if (s1.length !== s2.length) {
    return false;
  }

  let lookup = {};
  // counting for s1...
  for (let c of s1) {
    lookup[c] = (lookup[c] || 0) + 1;
  }

  // ... but deducting for s2
  for (let c of s2) {
    if (!lookup[c]) {
      return false;
    } else {
      lookup[c]--;
    }
  }

  return true;
}
