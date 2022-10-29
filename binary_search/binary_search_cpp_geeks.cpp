#include <iostream>
#include <vector>
using namespace std;


int binarySearch(vector<int> nums, int target){
    int lo = 0, hi = nums.size() - 1;
    int mid;

    while (lo <= hi){
        mid = (hi + lo) / 2;
        if (nums[mid]==target){
            return mid;
        }
        else if (nums[mid] < target) {
            lo = mid + 1;
        }
        else{
            hi = mid - 1;
        }
    }
    return -1;
}

int main(){
    vector<int> v = {1, 5, 10, 15, 28};
    int to_find = 28;
    cout<<binarySearch(v, to_find)<<'\n';
    to_find = 1;
    cout<<binarySearch(v, to_find)<<'\n';
    to_find = 100;
    cout<<binarySearch(v, to_find)<<'\n';
    return 0;
}