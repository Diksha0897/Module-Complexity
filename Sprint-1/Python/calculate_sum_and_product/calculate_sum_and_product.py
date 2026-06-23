from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity:O(n)
    Space Complexity: O(1)
    Optimal time complexity: O(n)
    """
    # Edge case: empty list
   
    if not input_numbers:
        return {"sum": 0, "product": 1}

    total_sum = 0
    product = 1

    for current_number in input_numbers:
        total_sum += current_number
        product *= current_number

    return {"sum": total_sum, "product": product}
