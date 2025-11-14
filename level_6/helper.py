def get_alt_waypoints(ast_x, ast_y, ss_x, ss_y, mode = 0):
    new_waypoints = [[ast_x, ast_y], [ast_x, ast_y]]
    inc = 3 if (mode % 2 == 0) else -3

    if mode < 2:
        if (abs(ast_y) < abs(ast_x)):
            new_waypoints[0][0] += inc if (0 > ast_x) else -inc
            new_waypoints[0][1] += inc if (ss_y > 0) else -inc

            new_waypoints[1][0] += -inc if (0 > ast_x) else inc
            new_waypoints[1][1] += inc if (ss_y > 0) else -inc

        else:
            new_waypoints[0][0] += inc if (0 > ast_x) else -inc
            new_waypoints[0][1] += -inc if (ss_y > 0) else inc

            new_waypoints[1][0] += inc if (0 > ast_x) else -inc
            new_waypoints[1][1] += inc if (ss_y > 0) else -inc

    if mode == 0:
        return new_waypoints
    if mode == 1:
        return [new_waypoints[1], new_waypoints[0]]

    if mode == 2:
        return [[ast_x, ast_y + 3]]
    if mode == 3:
        return [[ast_x, ast_y - 3]]
    if mode == 4:
        return [[ast_x + 3, ast_y + 3]]
    if mode == 5:
        return [[ast_x + 3, ast_y - 3]]
    if mode == 6:
        return [[ast_x + 3, ast_y]]
    if mode == 7:
        return [[ast_x - 3, ast_y + 3]]
    if mode == 8:
        return [[ast_x - 3, ast_y - 3]]
    if mode == 9:
        return [[ast_x - 3, ast_y]]
