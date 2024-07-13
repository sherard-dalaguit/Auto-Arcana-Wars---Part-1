from pathlib import Path


def read_data(team_assignment: Path):
    print(team_assignment.resolve())


if __name__ == "__main__":
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument("--team_assignment", 
                        type=str, 
                        help="The location of the team assignment file to read",
                        default="./team_assignments/assignment_1.json",
                        required=False)
    args = parser.parse_args()
    team_assignment = Path(args.team_assignment)
    read_data(team_assignment=team_assignment)
