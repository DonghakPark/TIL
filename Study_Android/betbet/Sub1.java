package com.donghakp.betbet;

"""
@Author : DongHak Park, 32151648
@Dankook University, Dept of Software
@Date : 2019-08-13
"""


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

import static com.donghakp.betbet.MainActivity.arr;
import static com.donghakp.betbet.MainActivity.len;

public class Sub1 extends AppCompatActivity {

    int CHECK_NUM[] ={0,0,0,0,0,0,0,0,0,0,0,0};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub1);

        final ImageButton bt1 = (ImageButton) findViewById(R.id.box1);
        final ImageButton bt2 = (ImageButton) findViewById(R.id.box2);
        final ImageButton bt3 = (ImageButton) findViewById(R.id.box3);
        final ImageButton bt4 = (ImageButton) findViewById(R.id.box4);
        final ImageButton bt5 = (ImageButton) findViewById(R.id.box5);
        final ImageButton bt6 = (ImageButton) findViewById(R.id.box6);
        final ImageButton bt7 = (ImageButton) findViewById(R.id.box7);
        final ImageButton bt8 = (ImageButton) findViewById(R.id.box8);
        final ImageButton bt9 = (ImageButton) findViewById(R.id.box9);
        final ImageButton bt10 = (ImageButton) findViewById(R.id.box10);
        final ImageButton bt11 = (ImageButton) findViewById(R.id.box11);
        final ImageButton bt12 = (ImageButton) findViewById(R.id.box12);

        for(int k = 0; k<len; k++)
        {
            if (arr[k] == 1)
                bt1.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 2)
                bt2.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 3)
                bt3.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 4)
                bt4.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 5)
                bt5.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 6)
                bt6.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 7)
                bt7.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 8)
                bt8.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 9)
                bt9.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 10)
                bt10.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 11)
                bt11.setBackgroundResource(R.drawable.checkbox_yes);
            else if (arr[k] == 12)
                bt12.setBackgroundResource(R.drawable.checkbox_yes);
            else
                break;
        }

        bt1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[0] ==0)
                {
                    bt1.setSelected(true);
                    CHECK_NUM[0] = 1;
                }
                else
                {
                    bt1.setSelected(false);
                    CHECK_NUM[0] =0;
                }

            }
        });
        bt2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[1] ==0)
                {
                    bt2.setSelected(true);
                    CHECK_NUM[1] = 1;
                }
                else
                {
                    bt2.setSelected(false);
                    CHECK_NUM[1] =0;
                }

            }
        });
        bt3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[2] ==0)
                {
                    bt3.setSelected(true);
                    CHECK_NUM[2] = 1;
                }
                else
                {
                    bt3.setSelected(false);
                    CHECK_NUM[2] =0;
                }

            }
        });
        bt4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[3] ==0)
                {
                    bt4.setSelected(true);
                    CHECK_NUM[3] = 1;
                }
                else
                {
                    bt4.setSelected(false);
                    CHECK_NUM[3] =0;
                }

            }
        });
        bt5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[4] ==0)
                {
                    bt5.setSelected(true);
                    CHECK_NUM[4] = 1;
                }
                else
                {
                    bt5.setSelected(false);
                    CHECK_NUM[4] =0;
                }

            }
        });
        bt6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[5] ==0)
                {
                    bt6.setSelected(true);
                    CHECK_NUM[5] = 1;
                }
                else
                {
                    bt6.setSelected(false);
                    CHECK_NUM[5] =0;
                }

            }
        });
        bt7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[6] ==0)
                {
                    bt7.setSelected(true);
                    CHECK_NUM[6] = 1;
                }
                else
                {
                    bt7.setSelected(false);
                    CHECK_NUM[6] =0;
                }

            }
        });
        bt8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[7] ==0)
                {
                    bt8.setSelected(true);
                    CHECK_NUM[7] = 1;
                }
                else
                {
                    bt8.setSelected(false);
                    CHECK_NUM[7] =0;
                }

            }
        });
        bt9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[8] ==0)
                {
                    bt9.setSelected(true);
                    CHECK_NUM[8] = 1;
                }
                else
                {
                    bt9.setSelected(false);
                    CHECK_NUM[8] =0;
                }

            }
        });
        bt10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[9] ==0)
                {
                    bt10.setSelected(true);
                    CHECK_NUM[9] = 1;
                }
                else
                {
                    bt10.setSelected(false);
                    CHECK_NUM[9] =0;
                }

            }
        });
        bt11.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[10] ==0)
                {
                    bt11.setSelected(true);
                    CHECK_NUM[10] = 1;
                }
                else
                {
                    bt11.setSelected(false);
                    CHECK_NUM[10] =0;
                }

            }
        });
        bt12.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(CHECK_NUM[11] ==0)
                {
                    bt12.setSelected(true);
                    CHECK_NUM[11] = 1;
                }
                else
                {
                    bt12.setSelected(false);
                    CHECK_NUM[11] =0;
                }

            }
        });

    }

}


