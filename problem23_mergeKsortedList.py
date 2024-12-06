import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        """
        Definition for a singly-linked list node.
        :param val: The value of the node.
        :param next: Pointer to the next node.
        """
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into a single sorted linked list.

        Approach:
        ---------
        - Use a min-heap (priority queue) to efficiently find the smallest element among the heads of the k lists.
        - Continuously extract the smallest element, append it to the merged list, and push the next element
          of the extracted list back into the heap.

        Time Complexity:
        ----------------
        O(N * log(k)), where:
        - N is the total number of nodes across all linked lists.
        - k is the number of linked lists.
        Each insertion or deletion operation in the heap takes O(log(k)) time.

        Space Complexity:
        -----------------
        O(k) for the heap, which stores at most k elements.

        :param lists: A list of linked-list heads, where each linked list is sorted.
        :return: The head of the merged sorted linked list.
        """

        # Initialize a min-heap to store (node value, list index, node reference)
        min_heap = []

        # Populate the heap with the first node of each linked list
        for index, linked_list in enumerate(lists):  # O(k)
            if linked_list:  # Ensure the list is non-empty
                heapq.heappush(min_heap, (linked_list.val, index, linked_list))
                # Push (node value, index of the linked list, node itself)

        # Create a dummy node to simplify the merged linked list construction
        dummy = ListNode(0)
        current = dummy  # Pointer to build the merged list

        # Extract the smallest elements from the heap until it is empty
        while min_heap:  # O(N * log(k))
            # Pop the smallest element (node with the smallest value)
            value, index, node = heapq.heappop(min_heap)
            
            # Append the node to the merged linked list
            current.next = node
            current = current.next  # Move the pointer forward
            
            # If the extracted node has a next node, push it into the heap
            if node.next:  # O(log(k))
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        # Return the head of the merged sorted linked list
        return dummy.next

# Example Usage:
# Input: lists = [[1->4->5], [1->3->4], [2->6]]
# Output: 1->1->2->3->4->4->5->6
