# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev_node = None
        non_reversed_tail_1 = None
        reversed_tail = None
        cur_node = head
        cur_index = 1
        non_reversed_head_2 = None

        while cur_node:
            # Set the tail of the non reverse first half
            if cur_index == left:
                non_reversed_tail_1 = prev_node
                reversed_tail = cur_node
            # Set the head of the non reversed second half
            if cur_index == right:
                non_reversed_head_2 = cur_node.next
            # If cur_index is in the reversed section, we have to start reversing
            if cur_index >= left and cur_index <= right:
                next_node = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node
            elif cur_index > right:
                # Sharp exit since we have reverse the middle section
                break
            else:
                prev_node = cur_node
                cur_node = cur_node.next
            cur_index += 1

        # attach the reversed tail to the non reversed second half head
        if reversed_tail:
            reversed_tail.next = non_reversed_head_2
        
        # attach the non reversed first half to the prev node if there is a non reversed tail first half
        # return the head in this situation since there is a non reversed first half so the head is the
        # same
        if non_reversed_tail_1:
            non_reversed_tail_1.next = prev_node
            return head
        else:
            # otherwise, we will just return the prev_node, which sits at the head of the reversed section
            return prev_node

        
        
        

        # 1. The state right as the 'while' loop breaks:
        # 0->    <-1<-2<-3    4->5->6
        # t        t     p   (h,c)

        # 2. Stitch 1: reversed_tail.next = non_reversed_head_2
        # 0->(1) (4)<-1<-2<-3   4->5->6
        # t           t     p  (h,c)

        # 3. Stitch 2: non_reversed_tail_1.next = prev_node
        # 0->(3) (4)<-1<-2<-3   4->5->6
        # t           t     p  (h,c)

        # 4. The flattened result
        # 0 -> 3 -> 2 -> 1 -> 4 -> 5 -> 6
        





        