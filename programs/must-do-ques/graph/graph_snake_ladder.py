# Time complexity of the above solution is O(N) as every cell is added and removed only once from queue.
# And a typical enqueue or dequeue operation takes O(1) time.


class QueueEntry(object):
    def __init__(self, v=0, dist=0):
        self.v = v
        self.dist = dist


def minimum_dice_throws(n, moves):
    # The graph has n vertices. Mark all the vertices as not visited
    visited = [False] * n
    # Create a queue for BFS
    queue = []
    # Mark the node 0 as visited and enqueue it
    visited[0] = True
    # Distance of 0't vertex is also 0 Enqueue 0'th vertex
    queue.append(QueueEntry(0, 0))
    # Do a BFS starting from vertex at index 0
    qe = QueueEntry()
    while queue:
        qe = queue.pop(0)
        v = qe.v
        if v == n - 1:
            break

        j = v + 1
        while j <= v + 6 and j < n:

            # If this cell is already visited,then ignore
            if visited[j] is False:
                # Otherwise calculate its distance and mark it as visited
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True

                # Check if there a snake or ladder at 'j' then tail of snake or top of ladder become the adjacent of 'i'
                a.v = moves[j] if moves[j] != -1 else j

                queue.append(a)

            j += 1

    return qe.dist


# n = 30
# moves = [-1] * n
#
# # Ladders starting index at 1
# moves[3] = 22
# moves[5] = 8
# moves[11] = 26
# moves[20] = 29
#
# # Snakes
# moves[27] = 1
# moves[21] = 9
# moves[17] = 4
# moves[19] = 9

n = 30
moves = [-1] * n

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

res = minimum_dice_throws(n, moves)
print(res)
