#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream file("input.txt");
    int calories[500]={}; //zakladamy "na oko", ze nie bedzie wiecej elfow
    int total = 0;
    int elf = 0;
    string line;

    //wczytanie i zsumowanie kalorii kazdego elfa
    while(!file.eof()){
        getline(file, line);
        if(line == ""){
            calories[elf] = total;
            elf++;
            total=0;
        }
        else
            total += stoi(line); //zamiana string -> int
    }
    calories[elf] = total;

    sort(calories, calories+elf+1, greater<int>());

    //for(int i=0; i<elf+1; i++)
    //    cout<<i<<" "<<calories[i]<<endl;

    cout<<"Part 1: "<<calories[0]<<endl;
    int top3 = calories[0]+calories[1]+calories[2];
    cout<<"Part 2: "<<top3<<endl;

}
