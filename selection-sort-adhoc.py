Tip/Note: Try sorting from last element if you are sorting from first element.
def selectionSort(ar,n):
    for i in range(n-1):
        maxi=0
        for j in range(1,n-i,1):
            if(ar[j]>ar[maxi]):
                maxi=j
        print(maxi, end=' ')
        ar[maxi], ar[n-1-i] = ar[n-1-i], ar[maxi]
    print()


k=int(input())
for i in range(k):
    n=int(input())
    ar=list(map(int, input().split()))[:n]
    selectionSort(ar,n)

// implementation in cpp
#include<bits/stdc++.h>
using namespace std;

void selection_sort(vector<int> &v, int n){
    for(int i=0;i<n-1;i++){
        int maxi = 0;
        for(int j=1;j<n-i;j++)
            if(v[j]>v[maxi])
                maxi = j;
        cout << maxi << " ";
        swap(v[n-i-1],v[maxi]);
    }
    cout << endl;
}

int main(){
    int t,n;
    cin >> t;
    while(t-->0){
        cin >> n;
        vector<int> v(n);
        for(int i=0;i<n;i++)
            cin >> v[i];
        selection_sort(v,n);
    }
    return 0;
}

// implementation in java
import java.util.*;

public class Main {
  static void selection_sort(int ar[], int n){
      for(int i=0;i<n-1;i++){
          int maxi = 0;
          for(int j=1;j<n-i;j++)
              if(ar[j]>ar[maxi])
                  maxi = j;
          System.out.printf("%d ",maxi);
          int t = ar[n-i-1];
          ar[n-i-1] = ar[maxi];
          ar[maxi] = t;
      }
      System.out.println();
  }

  public static void main(String [] args){
    Scanner sc = new Scanner(System.in);
    int t,n;
    t = sc.nextInt();
    while(t-->0){
      n = sc.nextInt();
      int ar[] = new int[n];
      for(int i=0;i<n;i++)
        ar[i] = sc.nextInt();
      selection_sort(ar,n);
    }
  }
}
