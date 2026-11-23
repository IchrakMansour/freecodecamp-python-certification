def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    result = []

    def record_state():
        result.append(f"{rod1} {rod2} {rod3}")

    def move_disks(count, source, auxiliary, target):
        if count == 0:
            return

        move_disks(count - 1, source, target, auxiliary)

        disk = source.pop()
        target.append(disk)

        record_state()

    
        move_disks(count - 1, auxiliary, source, target)

    
    record_state()


    move_disks(n, rod1, rod2, rod3)

    return "\n".join(result)