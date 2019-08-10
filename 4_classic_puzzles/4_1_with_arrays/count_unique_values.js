function countUniqueValues(arr) {
  if (arr.length > 1) {
    let left = 0; // pointer from the beginning
    let leftScout = 1; // pointer looking for the next different value

    while (leftScout < arr.length) {
      if (arr[leftScout] === arr[left]) {
        leftScout++;
      } else {
        left++;
        arr[left] = arr[leftScout];
        leftScout++;
      }
    }

    return left + 1;
  }

  return arr.length;
}
// Time complexity of 'countUniqueValues': O(n)
// Space compexity of 'countUniqueValues': O(1)
