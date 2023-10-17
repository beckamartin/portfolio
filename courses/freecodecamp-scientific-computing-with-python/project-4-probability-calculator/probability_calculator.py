import random
import copy

random.seed(95)

def main():
    hat = Hat(blue=3,red=2,green=6)

    probability = experiment(hat=hat,
                        expected_balls={"blue":2, "green":1},
                        num_balls_drawn=4,
                        num_experiments=1000)

    print(f"Probability = {probability}")

class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = []
        self.removed_contents = []

        for key, word in self.balls.items():
            for _ in range(word):
                self.contents.append(key)

    def draw(self, draw_num):
        contents_range = len(self.contents)
        
        if draw_num >= contents_range:
            for _ in range(0, contents_range):
                self.removed_contents.append(self.contents[_])
            return self.removed_contents

        else:
            for _ in range(draw_num):
                random_num = random.randint(0, contents_range - 1)
                self.removed_contents.append(self.contents[random_num])
                del self.contents[random_num]
                contents_range -= 1
            return self.removed_contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        searching = []

        for key, word in expected_balls.items():
            for _ in range(word):
                searching.append(key)

        result = hat_copy.draw(num_balls_drawn)

        for color in result:
            if color in searching:
                searching.remove(color)

        if searching == []:
            count += 1
 
    return count / num_experiments


if __name__ == "__main__":
    main()