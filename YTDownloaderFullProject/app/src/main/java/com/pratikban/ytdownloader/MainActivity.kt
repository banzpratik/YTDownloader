package com.pratikban.ytdownloader

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (! Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }
        val py = Python.getInstance()
        val pyObj = py.getModule("main")

        val input = findViewById<EditText>(R.id.inputUrl)
        val button = findViewById<Button>(R.id.downloadBtn)

        button.setOnClickListener {
            val url = input.text.toString()
            pyObj.callAttr("download_video", url)
        }
    }
}
