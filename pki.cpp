#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

// owner : CA
map<string, string> pki = {
    {"ЦС1", "Корневой ЦС"},
    {"ЦС2", "Корневой ЦС"},
    {"ЦС3", "ЦС1"},
    {"ЦС4", "ЦС1"},
    {"ЦС5", "ЦС2"},
    {"ЦС6", "ЦС2"},
    {"User 1", "ЦС3"},
    {"User 2", "ЦС4"},
    {"User 3", "ЦС4"},
    {"User 4", "ЦС5"},
    {"User 5", "ЦС6"},
    {"User 6", "ЦС6"},
};

void process_user(const string& id) {
    cout << "processing user \'" << id << "\'\n";
    vector<string> chain = {id};
    while (pki.count(chain.back())) {
        chain.push_back(pki.at(chain.back()));  
    }

    string del = "";
    for (auto& c : chain) {
        cout << del << c;
        del = " -> ";
    }
    cout << "\nResult: ";
    if (chain.back() == "Корневой ЦС") cout << "Real\n";
    else cout << "Fake\n";
    cout << "########################\n";
}

int main() {
    process_user("User 5");
    process_user("User 0");
}
