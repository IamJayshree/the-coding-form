#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define pb          push_back
#define endl        '\n'
#define hell		1000000007
#define all(a)      (a).begin(),(a).end()
#define deb(x)		cout << #x << " = " << x << endl

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while(T--){
    	int N, B, M;
    	cin >> N;
    	cin >> B;
    	cin >> M;

    	int arr[M];

    	for (int i = 0; i < M; ++i)
    		cin >> arr[i];

    	int totalB = N/B + 1;
    
    	int moved = 0;
    	int prev = 0;

    	for (int i = 0; i < M; ++i)
    	{
    		int curr = arr[i];
    	
    		int block = curr/B + 1;
    		if(block != prev){
    			moved++;
    			prev = block;
    	}
    	
    }
        cout << moved << endl;
    }
    return 0;
}
