#include <iostream>
#include <deque>

using namespace std;

class Teque {
private:
    deque<int> front;
    deque<int> back;

    // Balances the two deques to ensure they are nearly equal in size
    void balance() {
        if (front.size() > back.size() + 1) {
            back.push_front(front.back());
            front.pop_back();
        } else if (back.size() > front.size()) {
            front.push_back(back.front());
            back.pop_front();
        }
    }

public:
    void push_back(int value) {
        back.push_back(value);
        balance();
    }

    void push_front(int value) {
        front.push_front(value);
        balance();
    }

    void push_middle(int value) {
        if (front.size() == back.size()) {
            front.push_back(value);
        } else {
            back.push_front(value);
        }
        balance();
    }

    int get(int index) {
        if (index < front.size()) {
            return front[index];
        } else {
            return back[index - front.size()];
        }
    }
};

int main() {
    int operations;
    cin >> operations;
    
    Teque teque;
    
    for (int i = 0; i < operations; ++i) {
        string command;
        int value;
        cin >> command >> value;
        
        if (command == "push_back") {
            teque.push_back(value);
        } else if (command == "push_front") {
            teque.push_front(value);
        } else if (command == "push_middle") {
            teque.push_middle(value);
        } else if (command == "get") {
            cout << teque.get(value) << endl;
        }
    }

    return 0;
}
