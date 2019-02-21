
  <h1>Blockchain & Applications Assignment 2</h1>
  <p>A program that breaks SHA1 hashes in a brute force manner.</p>
  <h2>Breaking SHA1 hashes</h2>
<h4>How to run program?</h4>
  <ol>
    <li>Save files <strong><em>hashBreaker.py</em></strong> and <strong><em>wordCheck.txt</em></strong> in the same folder.</li>
    <li>Open terminal/cmd and go inside of the folder where the two files are saved.</li>
    <li>When running program. . .
    <ul><li>When checking one hash function enter command <strong><em>python hashBreaker.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3</em></strong>. The program will check the hash against the word bank to find a match. Once a match is found the program will show the attempts taken and list the word that created the hash. If no match is found there will be nothing shown.</li>
      <li>When checking a <a href="https://en.wikipedia.org/wiki/Salt_(cryptography)">salted hash</a>, enter the salted term hash first followed by the final hash. Enter command <strong><em>python hashBreaker.py f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ece4bb07f2580ed8b39aa52b7f7f918e43033ea1</em></strong>. The program will check the hash of the first input (salted term hash) with the word bank. When a match is found the program will take the salted term add a word from the word bank to it and create a hash. That hash is then checked against the final hash. Once a match is found the program will show the attempts taken and list the word that created the hash for the salted term and final hash. If no match is found there will be nothing shown.</li>
      </ul></li>
  </ol>
  <h4>Exercises</h4>
  <ol>
    <li>Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3</li>
    <li>Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31</li>
    <li> leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 <p>Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e this is concatenated before hashing with another word to produce the salted hash.</p></li>
    <li>graduate student: 34302959e138917ce9339c0b30ec50e650ce6b40 <p>Hint: This hash constitutes two terms separated by one space.</p></li>
  </ol>
  <h4>Solutions to exercises</h4>

