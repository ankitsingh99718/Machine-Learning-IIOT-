#include<stdio.h>
int main()
{
	int n, i, j;
	int bt[20], wt[20], tat[20], p[20];
	float avg_wt = 0, avg_tat = 0;
	int temp;

	printf("Enter number of processes: ");
	scanf("%d", &n);

    // Input burst times
	for(i = 0; i < n; i++)
	{
		printf("Enter Burst Time for P%d: ", i+1);
		scanf("%d", &bt[i]);
        p[i] = i + 1;   // process number
      }

    // Sorting according to burst time (SJF logic)
      for(i = 0; i < n-1; i++)
      {
      	for(j = i+1; j < n; j++)
      	{
      		if(bt[i] > bt[j])
      		{
                // swap burst time
      			temp = bt[i];
      			bt[i] = bt[j];
      			bt[j] = temp;

                // swap process number
      			temp = p[i];
      			p[i] = p[j];
      			p[j] = temp;
      		}
      	}
      }

    // Waiting time calculation
      wt[0] = 0;
      for(i = 1; i < n; i++)
      {
      	wt[i] = wt[i-1] + bt[i-1];
      }

    // Turnaround time calculation
      for(i = 0; i < n; i++)
      {
      	tat[i] = wt[i] + bt[i];
      	avg_wt += wt[i];
      	avg_tat += tat[i];
      }

    // Output
      printf("\nProcess Burst Time Waiting Time Turnaround Time\n");

      for(i = 0; i < n; i++)
      {
      	printf("P%d\t\t\t%d\t\t\t%d\t\t\t\t%d\n",
      		p[i], bt[i], wt[i], tat[i]);
      }

      printf("\nAverage Waiting Time = %.2f", avg_wt/n);
      printf("\nAverage Turnaround Time = %.2f", avg_tat/n);

      return 0;
    }