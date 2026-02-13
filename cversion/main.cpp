#include<random>

std::mt19937 rng(std::random_device{}());
std::uniform_int_distribution<int> dist(1, 5);

class Card {
public: 
    // Random vals for test to start with
    Card() : north(dist(rng)), 
             south(dist(rng)), 
             east(dist(rng)), 
             west(dist(rng)) {}

private:
    uint8_t north; 
    uint8_t south; 
    uint8_t east; 
    uint8_t west; 
};


class Board {
public: 
    Board() : gameover(false) {};

    bool is_gameover() { return gameover; }
    void set_gameover(bool val) { gameover = val; }
    void place_card() {}

private:
    bool gameover;
};


#include <vector>
using Hand = std::vector<Card>;


class HumanPlayer {
public:

private:
    Hand hand;
};


class IAgent {
public: 

private:
    Hand hand;
};


class GreedyAgent : IAgent {
public:

private:

};


class AstarAgent: IAgent {
public:

private:

};


class GameEngine {
public:
    GameEngine(Board b) : board(b) {
    }

private:
    Board board;
};


class GUI {};



