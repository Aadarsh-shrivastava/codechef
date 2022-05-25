#include <iostream>
typedef long long int ll;
using namespace std;

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        ll A[n], B[n], count = 0;
        for (ll i = 0; i < n; i++)
            cin >> A[i];
        for (ll i = 0; i < n; i++)
            cin >> B[i];

        for (ll i = 0; i < n; i++)
        {
            for (ll j = i + 1; j < n; j++)
            {
                if (A[i] == B[j] && B[i] == A[j])
                    count++;
            }
        }
        cout <<count<<'\n';
    }
    return 0;
}