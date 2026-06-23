/**
 * Finds common items between two arrays.
 *
 * Time Complexity:  O(n + m)
 * Space Complexity: O(m)
 * Optimal Time Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
/*export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];*/

export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);

  return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};
