# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list
        # reverse the second half
        # merge the two halves
        dummy = ListNode(-1, head)
        trailer = leader = dummy

        while leader and leader.next:
            trailer = trailer.next
            leader = leader.next.next
       
        #[-1,2,4,6,8]
        #          l
        #      t

        second_half_cur_node = trailer.next
        trailer.next = None
        second_half_prev_node = None
        # reverse the second half
        while second_half_cur_node:
            next_node = second_half_cur_node.next
            second_half_cur_node.next = second_half_prev_node
            second_half_prev_node = second_half_cur_node
            second_half_cur_node = next_node

        first_half_cur_node = dummy.next
        second_half_cur_node = second_half_prev_node

        while second_half_cur_node and first_half_cur_node:
            first_half_next_node = first_half_cur_node.next
            first_half_cur_node.next = second_half_cur_node
            second_half_next_node = second_half_cur_node.next
            second_half_cur_node.next = first_half_next_node
            first_half_cur_node = first_half_next_node
            second_half_cur_node = second_half_next_node

        # return dummy.next


        #[2  ,4  ]
        #     fc  fn
        #[10  ,8  ,6  ]
        #      sc   sn
        # [2,10,4,8,None]                 fn      
        #                                    sc  
        #                                    