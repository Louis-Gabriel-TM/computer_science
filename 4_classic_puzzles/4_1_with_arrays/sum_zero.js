/*
Puzzle Wording
==============
Write a function called 'sumZero' which accepts a sorted array of integers.
It shouyd returns the first pair where sum is 0 and 'undefined' if such a pair does not exist.
*/

function naiveSumZero(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; i < arr.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
}
// Time complexity of 'naiveSumZero': O(n**2)
// Space compexity of 'naiveSumZero': O(1)

function refactoredSumZero(arr) {
  let left = 0; // pointer from the beginning
  let right = arr.length - 1; // pointer from the end

  while (left < right) {
    let sum = arr[left] + arr[right];

    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}
// Time complexity of 'refactoredSumZero': O(n)
// Space compexity of 'refactoredSumZero': O(1)
