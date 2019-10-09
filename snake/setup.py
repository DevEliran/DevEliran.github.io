import cx_Freeze

executables=[cx_Freeze.Executable("snake.py")]
cx_Freeze.setup(name="Snake",
                 options={"build_exe":{"packages":["pygame"],
                                         "include_files":["snake.py",r"8.jpg","high_score.txt",r"1.mp3",r"2.mp3",r"1.jpg",r"2.jpg",r"3.jpg",r"4.jpg",r"5.jpg",r"6.jpg",r"7.jpg"
                                                            ]}},
                 executables=executables)
