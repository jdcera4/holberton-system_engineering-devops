<h1 class="gap">0x06. Regular expression</h1>
<div class="gap" id="project-description">
  <h2>Background Context</h2>

<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>

<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>

<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/SJ2eQ7V2iQlCgLc-L96zWg" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a> </li>
<li><a href="/rltoken/qyjWL-J1_qUaZGR690gH1Q" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a> </li>
<li><a href="/rltoken/WCjn8NgohbQ5NGXEObWZvQ" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a> </li>
<li><a href="/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a> </li>
<li><a href="/rltoken/Y-OVGcJ5cskdXWIBowiE_A" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env ruby</code></li>
<li>All your regex must be built for the Oniguruma library</li>
</ul>

</div>
<h2 class="gap" id="project-quiz-questions-title">
    Quiz questions
  </h2>
<div class="panel-body">
        <p id="quiz_questions_collapse_toggle">Hide</p>

      <section class="quiz_questions_show_container" style="display: block;">
          <div class="quiz_question_item_container" data-role="quiz_question436" data-position="2">
            <div class=" clearfix" id="quiz_question-436">

    <h4 class="quiz_question">Question #0</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What is the <code>/holberton/</code> regexp matching?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="436">
                <li class="">
  <input type="checkbox" name="quiz-answer-1506447957526" id="quiz-answer-1506447957526" data-quiz-question-id="436" data-quiz-answer-id="1506447957526" disabled="disabled">
  <label for="quiz-answer-1506447957526">
    <p>holbert0n</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506447966080" id="quiz-answer-1506447966080" data-quiz-question-id="436" data-quiz-answer-id="1506447966080" disabled="disabled">
  <label for="quiz-answer-1506447966080">
    <p>Holberton</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506447975582" id="quiz-answer-1506447975582" data-quiz-question-id="436" data-quiz-answer-id="1506447975582" disabled="disabled" checked="checked">
  <label for="quiz-answer-1506447975582">
    <p>holberton</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question437" data-position="3">
            <div class=" clearfix" id="quiz_question-437">

    <h4 class="quiz_question">Question #1</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What is the <code>/Holbert.n/</code> regexp matching?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="437">
                <li class="">
  <input type="checkbox" name="quiz-answer-1506447990910" id="quiz-answer-1506447990910" data-quiz-question-id="437" data-quiz-answer-id="1506447990910" disabled="disabled" checked="checked">
  <label for="quiz-answer-1506447990910">
    <p>Holbert.n</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506448010238" id="quiz-answer-1506448010238" data-quiz-question-id="437" data-quiz-answer-id="1506448010238" disabled="disabled" checked="checked">
  <label for="quiz-answer-1506448010238">
    <p>Holberton</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506448016293" id="quiz-answer-1506448016293" data-quiz-question-id="437" data-quiz-answer-id="1506448016293" disabled="disabled">
  <label for="quiz-answer-1506448016293">
    <p>holberton</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question438" data-position="4">
            <div class=" clearfix" id="quiz_question-438">

    <h4 class="quiz_question">Question #2</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What is the <code>/Holbert*n/</code> regexp matching?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="438">
                <li class="">
  <input type="checkbox" name="quiz-answer-1506448055190" id="quiz-answer-1506448055190" data-quiz-question-id="438" data-quiz-answer-id="1506448055190" disabled="disabled" checked="checked">
  <label for="quiz-answer-1506448055190">
    <p>Holberttn</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506448057879" id="quiz-answer-1506448057879" data-quiz-question-id="438" data-quiz-answer-id="1506448057879" disabled="disabled">
  <label for="quiz-answer-1506448057879">
    <p>Holberton</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1506448061984" id="quiz-answer-1506448061984" data-quiz-question-id="438" data-quiz-answer-id="1506448061984" disabled="disabled">
  <label for="quiz-answer-1506448061984">
    <p>Holbert.n</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>