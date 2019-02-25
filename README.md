
  <h1>Blockchain & Applications</h1>
  <p>A program that breaks SHA1 hashes in a brute force manner.</p>
  <h2>Breaking SHA1 hashes</h2>
  <h4>About My Code</h4>
  <p>This code imported three libraries: <a href = "https://docs.python.org/2/library/hashlib.html" title ="HashLib Info">hashlib</a>, <a href = "https://docs.python.org/2/library/sys.html" title ="Sys Info">sys</a>, and <a href ="https://docs.python.org/2/library/time.html" title = "Time Info">time</a>. The hashlib library offers many different secure hash and message digest algorithms. The hash algorithm used for this program was SHA1. The sys library was used to grab the input from the user as an argument. The argument(s) will be the SHA1 hash that the user wants to break with brute force. The time library was used to keep track of how long the program took to run from start to end. When the program starts, it checks the amount of arguments to see how many values there are. The program will throw an error if there are less than one or more than three values entered. If there are two values in the arguments, the program will grab the hash (the second value) and begin brutally attacking the hash against one million words/numbers/phrases. If there are three values, the second value is checked against the word bank to find a match. When there is a match with the second value, the root word is then concatenated with each word in the word bank to find what hash matches the third value the user entered. The program will display the attempts taken at cracking the hash, the root word that made the hash, and the time it took to find its match.</p>
<h4>How to run program?</h4>
  <ol>
    <li>Save files <strong><em>hashBreaker.py</em></strong> and <strong><em>wordCheck.txt</em></strong> in the same folder.</li>
  <li>Open terminal/cmd and go inside of the folder where the two files are saved.</li>
    <li>When running program. . .
    <ul><li>When checking one hash function enter command:<br><strong><em>python hashBreaker.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3</em></strong><br>The program will check the hash against the word bank to find a match. Once a match is found the program will show the attempts taken and list the word that created the hash. If no match is found there will be nothing shown.</li>
      <li>When checking a <a href="https://en.wikipedia.org/wiki/Salt_(cryptography)" title ="Salted Hash Info">salted hash</a>, enter the salted term hash first followed by the final hash. Enter command:<br><strong><em>python hashBreaker.py f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ece4bb07f2580ed8b39aa52b7f7f918e43033ea1</em></strong><br>The program will check the hash of the first input (salted term hash) with the word bank. When a match is found the program will take the salted term, add a word from the word bank to it, and create a hash. That hash is then checked against the final hash. Once a match is found the program will show the attempts taken and list the words that created the hash for the salted term and final hash. If no match is found there will be nothing shown.</li>
      </ul></li>
  </ol>
  <h4>Exercises</h4>
  <ol>
    <li>Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3</li>
    <li>Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31</li>
    <li> leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 <br>Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e this is concatenated before hashing with another word to produce the salted hash.</li>
  </ol>
  <h4>Solutions to exercises</h4>
  <ol>
  <li>Found Hash Match<br>Number of Attempts: 15<br>Match Word: letmein<br>Program runtime is: 0.0766329</li>
  <li>Found Hash Match<br>Number of Attempts: 999967<br>Match Word: vjhtrhsvdctcegth<br>Program runtime is: 2.4387748</li>
  <li>Found Hash Match<br>Number of Attempts: 216<br>Match Word: slayer<br>Found Final Hash Match<br>Number of Attempts: 546154<br>Match Word: slayerharib<br>Program runtime is: 1.3684120</li>
</ol>
<strong><em>Anthony Davis Assignment 2 for Blockchain and Applications</em></strong>
