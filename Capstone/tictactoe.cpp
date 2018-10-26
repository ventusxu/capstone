#include <vector>
#include <pair>
#include <iostream>

using namespace std;

class TicTacToe {
    
    int dim;
    vector<pair<int, int>> rows;
    vector<pair<int, int>> cols;
    vector<pair<int, int>> diags;

public:
    /** Initialize your data structure here. */
    TicTacToe(int n) : 
        dim(n),
        rows(vector<pair<int, int>> (n, {0, 0})),
        cols(vector<pair<int, int>> (n, {0, 0})),
        diags(vector<pair<int, int>> (2, {0, 0})) 
    {}
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        rows[row].first += 1;
        rows[row].second += player;
        cols[col].first += 1;
        cols[col].second += player;
        if (row == col)
        {
            diags[0].first += 1;
            diags[0].second += player;
        }
        if (row + col == dim - 1)
        {
            diags[1].first += 1;
            diags[1].second += player;
        }
        return win(row, col, player);
    }

    int win(int row, int col, int player) {
        bool rowWin = (rows[row].first == dim) && (rows[row].first * player == rows[row].second);
        bool colWin = (cols[col].first == dim) && (cols[col].first * player == cols[col].second);
        bool diagWin = false;
        if (row == col)
            diagWin = (diags[0].first == dim) && (diags[0].first * player == diags[0].second);
        if (row + col == dim - 1)
            diagWin |= (diags[1].first == dim) && (diags[1].first * player == diags[1].second);
        return (rowWin || colWin || diagWin) ? player : 0;
    }
};

int main() 
{
    TicTacToe ttt(2);
    cout << ttt.move(0,1,1) << " " << ttt.move(1,1,2) << " " << ttt.move(1,0,1) << endl;
}