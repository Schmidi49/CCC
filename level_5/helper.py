def get_alt_waypoints(ast_x, ast_y, ss_x, ss_y):
    new_waypoints = [[ast_x, ast_y], [ast_x, ast_y]]

    if (abs(ast_y) < abs(ast_x)):
        new_waypoints[0][0] += 3 if (0 > ast_x) else -3
        new_waypoints[0][1] += 3 if (ss_y > 0) else -3

        new_waypoints[1][0] += -3 if (0 > ast_x) else 3
        new_waypoints[1][1] += 3 if (ss_y > 0) else -3

    else:
        new_waypoints[0][0] += 3 if (0 > ast_x) else -3
        new_waypoints[0][1] += -3 if (ss_y > 0) else 3

        new_waypoints[1][0] += 3 if (0 > ast_x) else -3
        new_waypoints[1][1] += 3 if (ss_y > 0) else -3

    return new_waypoints
