package com.donghakp.betbet;

"""
@Author : DongHak Park, 32151648
@Dankook University, Dept of Software
@Date : 2019-08-13
"""

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.gms.ads.MobileAds;
import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;

public class MainActivity extends AppCompatActivity {
    private AdView mAdView;
    static int arr[];
    static int len;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        MobileAds.initialize(this, "-----insert key -----");
        mAdView = findViewById(R.id.adView);
        AdRequest adRequest = new AdRequest.Builder().build();
        mAdView.loadAd(adRequest);

        Button button = (Button) findViewById(R.id.start_button);
        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){

                Intent intent = new Intent(getApplicationContext(),Sub1.class);
                startActivity(intent);
            }
        });
    }
    public void make_num(View v){
        EditText number1 = (EditText) findViewById(R.id.input_num);
        int n1 = Integer.parseInt(number1.getText().toString());
        int rd[] = new int[n1];

        for(int i=0; i<n1; i++)
        {
            rd[i] = (int)(Math.random()*12+1);
            for(int j=0; j<i; j++)
            {
                if(rd[j]==rd[i])
                {
                    i--;
                    break;
                }
            }
        }
        arr = new int[n1];
        for(int k =0; k<n1; k++)
        {
            arr[k] = rd[k];
        }
        len = n1;
    }
}
