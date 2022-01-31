"
Command-line tool to remind daily tasks
"
#bro wtf is going on man
#part 2 commit test
#part 3 commit test
#part 4 commit test

#lol

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='check daily tasks')
    parser.add_argument('task',
                        help='task to use')

    parser.add_argument('--add', '-a',
                        help='Add to list',
                        action='store_true')
        
    parser.add_argument('--list', '-l'
                        help='check to-do list',
                        action='store_true')


    args = parser.parse_args()

    if args.list:
        with open('todolist.txt','w') as f:
            f_contents = f.read()
            print(f_contents)

