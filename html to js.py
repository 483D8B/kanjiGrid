import xml.etree.ElementTree as ET
import json

# Your HTML string
html = """
    <div class="divTable" id="kanji_table">
        <div class="divTableBody" id="table_body">
            <!-- Data will be inserted here -->

            <div class="divTableCell" id="1">
                <div class="framenr">1</div>
                <div class="kanji">一</div>
                <div class="keyword" style="display: none">one</div>
            </div>

            <div class="divTableCell" id="2">
                <div class="framenr">2</div>
                <div class="kanji">二</div>
                <div class="keyword" style="display: none">two</div>
            </div>

            <div class="divTableCell" id="3">
                <div class="framenr">3</div>
                <div class="kanji">三</div>
                <div class="keyword" style="display: none">three</div>
            </div>

            <div class="divTableCell" id="4">
                <div class="framenr">4</div>
                <div class="kanji">四</div>
                <div class="keyword" style="display: none">four</div>
            </div>

            <div class="divTableCell" id="5">
                <div class="framenr">5</div>
                <div class="kanji">五</div>
                <div class="keyword" style="display: none">five</div>
            </div>

            <div class="divTableCell" id="6">
                <div class="framenr">6</div>
                <div class="kanji">六</div>
                <div class="keyword" style="display: none">six</div>
            </div>

            <div class="divTableCell" id="7">
                <div class="framenr">7</div>
                <div class="kanji">七</div>
                <div class="keyword" style="display: none">seven</div>
            </div>

            <div class="divTableCell" id="8">
                <div class="framenr">8</div>
                <div class="kanji">八</div>
                <div class="keyword" style="display: none">eight</div>
            </div>

            <div class="divTableCell" id="9">
                <div class="framenr">9</div>
                <div class="kanji">九</div>
                <div class="keyword" style="display: none">nine</div>
            </div>

            <div class="divTableCell" id="10">
                <div class="framenr">10</div>
                <div class="kanji">十</div>
                <div class="keyword" style="display: none">ten</div>
            </div>

            <div class="divTableCell" id="11">
                <div class="framenr">11</div>
                <div class="kanji">口</div>
                <div class="keyword" style="display: none">mouth</div>
            </div>

            <div class="divTableCell" id="12">
                <div class="framenr">12</div>
                <div class="kanji">日</div>
                <div class="keyword" style="display: none">day</div>
            </div>

            <div class="divTableCell" id="13">
                <div class="framenr">13</div>
                <div class="kanji">月</div>
                <div class="keyword" style="display: none">month</div>
            </div>

            <div class="divTableCell" id="14">
                <div class="framenr">14</div>
                <div class="kanji">田</div>
                <div class="keyword" style="display: none">rice field</div>
            </div>

            <div class="divTableCell" id="15">
                <div class="framenr">15</div>
                <div class="kanji">目</div>
                <div class="keyword" style="display: none">eye</div>
            </div>

            <div class="divTableCell" id="16">
                <div class="framenr">16</div>
                <div class="kanji">古</div>
                <div class="keyword" style="display: none">old</div>
            </div>

            <div class="divTableCell" id="17">
                <div class="framenr">17</div>
                <div class="kanji">吾</div>
                <div class="keyword" style="display: none">I</div>
            </div>

            <div class="divTableCell" id="18">
                <div class="framenr">18</div>
                <div class="kanji">冒</div>
                <div class="keyword" style="display: none">risk</div>
            </div>

            <div class="divTableCell" id="19">
                <div class="framenr">19</div>
                <div class="kanji">朋</div>
                <div class="keyword" style="display: none">companion</div>
            </div>

            <div class="divTableCell" id="20">
                <div class="framenr">20</div>
                <div class="kanji">明</div>
                <div class="keyword" style="display: none">bright</div>
            </div>

            <div class="divTableCell" id="21">
                <div class="framenr">21</div>
                <div class="kanji">唱</div>
                <div class="keyword" style="display: none">chant</div>
            </div>

            <div class="divTableCell" id="22">
                <div class="framenr">22</div>
                <div class="kanji">晶</div>
                <div class="keyword" style="display: none">sparkle</div>
            </div>

            <div class="divTableCell" id="23">
                <div class="framenr">23</div>
                <div class="kanji">品</div>
                <div class="keyword" style="display: none">goods</div>
            </div>

            <div class="divTableCell" id="24">
                <div class="framenr">24</div>
                <div class="kanji">呂</div>
                <div class="keyword" style="display: none">spine</div>
            </div>

            <div class="divTableCell" id="25">
                <div class="framenr">25</div>
                <div class="kanji">昌</div>
                <div class="keyword" style="display: none">prosperous</div>
            </div>

            <div class="divTableCell" id="26">
                <div class="framenr">26</div>
                <div class="kanji">早</div>
                <div class="keyword" style="display: none">early</div>
            </div>

            <div class="divTableCell" id="27">
                <div class="framenr">27</div>
                <div class="kanji">旭</div>
                <div class="keyword" style="display: none">rising sun</div>
            </div>

            <div class="divTableCell" id="28">
                <div class="framenr">28</div>
                <div class="kanji">世</div>
                <div class="keyword" style="display: none">generation</div>
            </div>

            <div class="divTableCell" id="29">
                <div class="framenr">29</div>
                <div class="kanji">胃</div>
                <div class="keyword" style="display: none">stomach</div>
            </div>

            <div class="divTableCell" id="30">
                <div class="framenr">30</div>
                <div class="kanji">旦</div>
                <div class="keyword" style="display: none">nightbreak</div>
            </div>

            <div class="divTableCell" id="31">
                <div class="framenr">31</div>
                <div class="kanji">胆</div>
                <div class="keyword" style="display: none">gall bladder</div>
            </div>

            <div class="divTableCell" id="32">
                <div class="framenr">32</div>
                <div class="kanji">亘</div>
                <div class="keyword" style="display: none">span</div>
            </div>

            <div class="divTableCell" id="33">
                <div class="framenr">33</div>
                <div class="kanji">凹</div>
                <div class="keyword" style="display: none">concave</div>
            </div>

            <div class="divTableCell" id="34">
                <div class="framenr">34</div>
                <div class="kanji">凸</div>
                <div class="keyword" style="display: none">convex</div>
            </div>

            <div class="divTableCell" id="35">
                <div class="framenr">35</div>
                <div class="kanji">旧</div>
                <div class="keyword" style="display: none">olden times</div>
            </div>

            <div class="divTableCell" id="36">
                <div class="framenr">36</div>
                <div class="kanji">自</div>
                <div class="keyword" style="display: none">oneself</div>
            </div>

            <div class="divTableCell" id="37">
                <div class="framenr">37</div>
                <div class="kanji">白</div>
                <div class="keyword" style="display: none">white</div>
            </div>

            <div class="divTableCell" id="38">
                <div class="framenr">38</div>
                <div class="kanji">百</div>
                <div class="keyword" style="display: none">hundred</div>
            </div>

            <div class="divTableCell" id="39">
                <div class="framenr">39</div>
                <div class="kanji">中</div>
                <div class="keyword" style="display: none">in</div>
            </div>

            <div class="divTableCell" id="40">
                <div class="framenr">40</div>
                <div class="kanji">千</div>
                <div class="keyword" style="display: none">thousand</div>
            </div>

            <div class="divTableCell" id="41">
                <div class="framenr">41</div>
                <div class="kanji">舌</div>
                <div class="keyword" style="display: none">tongue</div>
            </div>

            <div class="divTableCell" id="42">
                <div class="framenr">42</div>
                <div class="kanji">升</div>
                <div class="keyword" style="display: none">measuring box</div>
            </div>

            <div class="divTableCell" id="43">
                <div class="framenr">43</div>
                <div class="kanji">昇</div>
                <div class="keyword" style="display: none">rise up</div>
            </div>

            <div class="divTableCell" id="44">
                <div class="framenr">44</div>
                <div class="kanji">丸</div>
                <div class="keyword" style="display: none">round</div>
            </div>

            <div class="divTableCell" id="45">
                <div class="framenr">45</div>
                <div class="kanji">寸</div>
                <div class="keyword" style="display: none">measurement</div>
            </div>

            <div class="divTableCell" id="46">
                <div class="framenr">46</div>
                <div class="kanji">肘</div>
                <div class="keyword" style="display: none">elbow</div>
            </div>

            <div class="divTableCell" id="47">
                <div class="framenr">47</div>
                <div class="kanji">専</div>
                <div class="keyword" style="display: none">specialty</div>
            </div>

            <div class="divTableCell" id="48">
                <div class="framenr">48</div>
                <div class="kanji">博</div>
                <div class="keyword" style="display: none">Dr.</div>
            </div>

            <div class="divTableCell" id="49">
                <div class="framenr">49</div>
                <div class="kanji">占</div>
                <div class="keyword" style="display: none">fortune-telling</div>
            </div>

            <div class="divTableCell" id="50">
                <div class="framenr">50</div>
                <div class="kanji">上</div>
                <div class="keyword" style="display: none">above</div>
            </div>

            <div class="divTableCell" id="51">
                <div class="framenr">51</div>
                <div class="kanji">下</div>
                <div class="keyword" style="display: none">below</div>
            </div>

            <div class="divTableCell" id="52">
                <div class="framenr">52</div>
                <div class="kanji">卓</div>
                <div class="keyword" style="display: none">eminent</div>
            </div>

            <div class="divTableCell" id="53">
                <div class="framenr">53</div>
                <div class="kanji">朝</div>
                <div class="keyword" style="display: none">morning</div>
            </div>

            <div class="divTableCell" id="54">
                <div class="framenr">54</div>
                <div class="kanji">嘲</div>
                <div class="keyword" style="display: none">derision</div>
            </div>

            <div class="divTableCell" id="55">
                <div class="framenr">55</div>
                <div class="kanji">只</div>
                <div class="keyword" style="display: none">only</div>
            </div>

            <div class="divTableCell" id="56">
                <div class="framenr">56</div>
                <div class="kanji">貝</div>
                <div class="keyword" style="display: none">shellfish</div>
            </div>

            <div class="divTableCell" id="57">
                <div class="framenr">57</div>
                <div class="kanji">唄</div>
                <div class="keyword" style="display: none">pop song</div>
            </div>

            <div class="divTableCell" id="58">
                <div class="framenr">58</div>
                <div class="kanji">貞</div>
                <div class="keyword" style="display: none">upright</div>
            </div>

            <div class="divTableCell" id="59">
                <div class="framenr">59</div>
                <div class="kanji">員</div>
                <div class="keyword" style="display: none">employee</div>
            </div>

            <div class="divTableCell" id="60">
                <div class="framenr">60</div>
                <div class="kanji">貼</div>
                <div class="keyword" style="display: none">post a bill(stick)</div>
            </div>

            <div class="divTableCell" id="61">
                <div class="framenr">61</div>
                <div class="kanji">見</div>
                <div class="keyword" style="display: none">see</div>
            </div>

            <div class="divTableCell" id="62">
                <div class="framenr">62</div>
                <div class="kanji">児</div>
                <div class="keyword" style="display: none">newborn babe</div>
            </div>

            <div class="divTableCell" id="63">
                <div class="framenr">63</div>
                <div class="kanji">元</div>
                <div class="keyword" style="display: none">beginning</div>
            </div>

            <div class="divTableCell" id="64">
                <div class="framenr">64</div>
                <div class="kanji">頁</div>
                <div class="keyword" style="display: none">page</div>
            </div>

            <div class="divTableCell" id="65">
                <div class="framenr">65</div>
                <div class="kanji">頑</div>
                <div class="keyword" style="display: none">stubborn</div>
            </div>

            <div class="divTableCell" id="66">
                <div class="framenr">66</div>
                <div class="kanji">凡</div>
                <div class="keyword" style="display: none">mediocre</div>
            </div>

            <div class="divTableCell" id="67">
                <div class="framenr">67</div>
                <div class="kanji">負</div>
                <div class="keyword" style="display: none">defeat</div>
            </div>

            <div class="divTableCell" id="68">
                <div class="framenr">68</div>
                <div class="kanji">万</div>
                <div class="keyword" style="display: none">ten thousand</div>
            </div>

            <div class="divTableCell" id="69">
                <div class="framenr">69</div>
                <div class="kanji">句</div>
                <div class="keyword" style="display: none">phrase</div>
            </div>

            <div class="divTableCell" id="70">
                <div class="framenr">70</div>
                <div class="kanji">肌</div>
                <div class="keyword" style="display: none">texture</div>
            </div>

            <div class="divTableCell" id="71">
                <div class="framenr">71</div>
                <div class="kanji">旬</div>
                <div class="keyword" style="display: none">decameron</div>
            </div>

            <div class="divTableCell" id="72">
                <div class="framenr">72</div>
                <div class="kanji">勺</div>
                <div class="keyword" style="display: none">ladle</div>
            </div>

            <div class="divTableCell" id="73">
                <div class="framenr">73</div>
                <div class="kanji">的</div>
                <div class="keyword" style="display: none">bull's eye</div>
            </div>

            <div class="divTableCell" id="74">
                <div class="framenr">74</div>
                <div class="kanji">首</div>
                <div class="keyword" style="display: none">neck</div>
            </div>

            <div class="divTableCell" id="75">
                <div class="framenr">75</div>
                <div class="kanji">乙</div>
                <div class="keyword" style="display: none">fish guts</div>
            </div>

            <div class="divTableCell" id="76">
                <div class="framenr">76</div>
                <div class="kanji">乱</div>
                <div class="keyword" style="display: none">riot</div>
            </div>

            <div class="divTableCell" id="77">
                <div class="framenr">77</div>
                <div class="kanji">直</div>
                <div class="keyword" style="display: none">straightaway</div>
            </div>

            <div class="divTableCell" id="78">
                <div class="framenr">78</div>
                <div class="kanji">具</div>
                <div class="keyword" style="display: none">tool</div>
            </div>

            <div class="divTableCell" id="79">
                <div class="framenr">79</div>
                <div class="kanji">真</div>
                <div class="keyword" style="display: none">true</div>
            </div>

            <div class="divTableCell" id="80">
                <div class="framenr">80</div>
                <div class="kanji">工</div>
                <div class="keyword" style="display: none">craft</div>
            </div>

            <div class="divTableCell" id="81">
                <div class="framenr">81</div>
                <div class="kanji">左</div>
                <div class="keyword" style="display: none">left</div>
            </div>

            <div class="divTableCell" id="82">
                <div class="framenr">82</div>
                <div class="kanji">右</div>
                <div class="keyword" style="display: none">right</div>
            </div>

            <div class="divTableCell" id="83">
                <div class="framenr">83</div>
                <div class="kanji">有</div>
                <div class="keyword" style="display: none">possess</div>
            </div>

            <div class="divTableCell" id="84">
                <div class="framenr">84</div>
                <div class="kanji">賄</div>
                <div class="keyword" style="display: none">bribe</div>
            </div>

            <div class="divTableCell" id="85">
                <div class="framenr">85</div>
                <div class="kanji">貢</div>
                <div class="keyword" style="display: none">tribute</div>
            </div>

            <div class="divTableCell" id="86">
                <div class="framenr">86</div>
                <div class="kanji">項</div>
                <div class="keyword" style="display: none">paragraph</div>
            </div>

            <div class="divTableCell" id="87">
                <div class="framenr">87</div>
                <div class="kanji">刀</div>
                <div class="keyword" style="display: none">sword</div>
            </div>

            <div class="divTableCell" id="88">
                <div class="framenr">88</div>
                <div class="kanji">刃</div>
                <div class="keyword" style="display: none">blade</div>
            </div>

            <div class="divTableCell" id="89">
                <div class="framenr">89</div>
                <div class="kanji">切</div>
                <div class="keyword" style="display: none">cut</div>
            </div>

            <div class="divTableCell" id="90">
                <div class="framenr">90</div>
                <div class="kanji">召</div>
                <div class="keyword" style="display: none">seduce</div>
            </div>

            <div class="divTableCell" id="91">
                <div class="framenr">91</div>
                <div class="kanji">昭</div>
                <div class="keyword" style="display: none">shining</div>
            </div>

            <div class="divTableCell" id="92">
                <div class="framenr">92</div>
                <div class="kanji">則</div>
                <div class="keyword" style="display: none">rule</div>
            </div>

            <div class="divTableCell" id="93">
                <div class="framenr">93</div>
                <div class="kanji">副</div>
                <div class="keyword" style="display: none">vice-</div>
            </div>

            <div class="divTableCell" id="94">
                <div class="framenr">94</div>
                <div class="kanji">別</div>
                <div class="keyword" style="display: none">separate</div>
            </div>

            <div class="divTableCell" id="95">
                <div class="framenr">95</div>
                <div class="kanji">丁</div>
                <div class="keyword" style="display: none">street</div>
            </div>

            <div class="divTableCell" id="96">
                <div class="framenr">96</div>
                <div class="kanji">町</div>
                <div class="keyword" style="display: none">village(small town)</div>
            </div>

            <div class="divTableCell" id="97">
                <div class="framenr">97</div>
                <div class="kanji">可</div>
                <div class="keyword" style="display: none">can</div>
            </div>

            <div class="divTableCell" id="98">
                <div class="framenr">98</div>
                <div class="kanji">頂</div>
                <div class="keyword" style="display: none">place on the head</div>
            </div>

            <div class="divTableCell" id="99">
                <div class="framenr">99</div>
                <div class="kanji">子</div>
                <div class="keyword" style="display: none">child</div>
            </div>

            <div class="divTableCell" id="100">
                <div class="framenr">100</div>
                <div class="kanji">孔</div>
                <div class="keyword" style="display: none">cavity</div>
            </div>

            <div class="divTableCell" id="101">
                <div class="framenr">101</div>
                <div class="kanji">了</div>
                <div class="keyword" style="display: none">complete</div>
            </div>

            <div class="divTableCell" id="102">
                <div class="framenr">102</div>
                <div class="kanji">女</div>
                <div class="keyword" style="display: none">woman</div>
            </div>

            <div class="divTableCell" id="103">
                <div class="framenr">103</div>
                <div class="kanji">好</div>
                <div class="keyword" style="display: none">fond</div>
            </div>

            <div class="divTableCell" id="104">
                <div class="framenr">104</div>
                <div class="kanji">如</div>
                <div class="keyword" style="display: none">likeness</div>
            </div>

            <div class="divTableCell" id="105">
                <div class="framenr">105</div>
                <div class="kanji">母</div>
                <div class="keyword" style="display: none">mama</div>
            </div>

            <div class="divTableCell" id="106">
                <div class="framenr">106</div>
                <div class="kanji">貫</div>
                <div class="keyword" style="display: none">pierce</div>
            </div>

            <div class="divTableCell" id="107">
                <div class="framenr">107</div>
                <div class="kanji">兄</div>
                <div class="keyword" style="display: none">elder brother</div>
            </div>

            <div class="divTableCell" id="108">
                <div class="framenr">108</div>
                <div class="kanji">呪</div>
                <div class="keyword" style="display: none">curse</div>
            </div>

            <div class="divTableCell" id="109">
                <div class="framenr">109</div>
                <div class="kanji">克</div>
                <div class="keyword" style="display: none">overcome</div>
            </div>

            <div class="divTableCell" id="110">
                <div class="framenr">110</div>
                <div class="kanji">小</div>
                <div class="keyword" style="display: none">little</div>
            </div>

            <div class="divTableCell" id="111">
                <div class="framenr">111</div>
                <div class="kanji">少</div>
                <div class="keyword" style="display: none">few</div>
            </div>

            <div class="divTableCell" id="112">
                <div class="framenr">112</div>
                <div class="kanji">大</div>
                <div class="keyword" style="display: none">large</div>
            </div>

            <div class="divTableCell" id="113">
                <div class="framenr">113</div>
                <div class="kanji">多</div>
                <div class="keyword" style="display: none">many</div>
            </div>

            <div class="divTableCell" id="114">
                <div class="framenr">114</div>
                <div class="kanji">夕</div>
                <div class="keyword" style="display: none">evening</div>
            </div>

            <div class="divTableCell" id="115">
                <div class="framenr">115</div>
                <div class="kanji">汐</div>
                <div class="keyword" style="display: none">eventide</div>
            </div>

            <div class="divTableCell" id="116">
                <div class="framenr">116</div>
                <div class="kanji">外</div>
                <div class="keyword" style="display: none">outside</div>
            </div>

            <div class="divTableCell" id="117">
                <div class="framenr">117</div>
                <div class="kanji">名</div>
                <div class="keyword" style="display: none">name</div>
            </div>

            <div class="divTableCell" id="118">
                <div class="framenr">118</div>
                <div class="kanji">石</div>
                <div class="keyword" style="display: none">stone</div>
            </div>

            <div class="divTableCell" id="119">
                <div class="framenr">119</div>
                <div class="kanji">肖</div>
                <div class="keyword" style="display: none">resemblance</div>
            </div>

            <div class="divTableCell" id="120">
                <div class="framenr">120</div>
                <div class="kanji">硝</div>
                <div class="keyword" style="display: none">nitrate</div>
            </div>

            <div class="divTableCell" id="121">
                <div class="framenr">121</div>
                <div class="kanji">砕</div>
                <div class="keyword" style="display: none">smash</div>
            </div>

            <div class="divTableCell" id="122">
                <div class="framenr">122</div>
                <div class="kanji">砂</div>
                <div class="keyword" style="display: none">sand</div>
            </div>

            <div class="divTableCell" id="123">
                <div class="framenr">123</div>
                <div class="kanji">妬</div>
                <div class="keyword" style="display: none">jealous</div>
            </div>

            <div class="divTableCell" id="124">
                <div class="framenr">124</div>
                <div class="kanji">削</div>
                <div class="keyword" style="display: none">plane</div>
            </div>

            <div class="divTableCell" id="125">
                <div class="framenr">125</div>
                <div class="kanji">光</div>
                <div class="keyword" style="display: none">ray</div>
            </div>

            <div class="divTableCell" id="126">
                <div class="framenr">126</div>
                <div class="kanji">太</div>
                <div class="keyword" style="display: none">plump</div>
            </div>

            <div class="divTableCell" id="127">
                <div class="framenr">127</div>
                <div class="kanji">器</div>
                <div class="keyword" style="display: none">utensil</div>
            </div>

            <div class="divTableCell" id="128">
                <div class="framenr">128</div>
                <div class="kanji">臭</div>
                <div class="keyword" style="display: none">stinking</div>
            </div>

            <div class="divTableCell" id="129">
                <div class="framenr">129</div>
                <div class="kanji">嗅</div>
                <div class="keyword" style="display: none">sniff</div>
            </div>

            <div class="divTableCell" id="130">
                <div class="framenr">130</div>
                <div class="kanji">妙</div>
                <div class="keyword" style="display: none">exquisite</div>
            </div>

            <div class="divTableCell" id="131">
                <div class="framenr">131</div>
                <div class="kanji">省</div>
                <div class="keyword" style="display: none">focus</div>
            </div>

            <div class="divTableCell" id="132">
                <div class="framenr">132</div>
                <div class="kanji">厚</div>
                <div class="keyword" style="display: none">thick</div>
            </div>

            <div class="divTableCell" id="133">
                <div class="framenr">133</div>
                <div class="kanji">奇</div>
                <div class="keyword" style="display: none">strange</div>
            </div>

            <div class="divTableCell" id="134">
                <div class="framenr">134</div>
                <div class="kanji">川</div>
                <div class="keyword" style="display: none">stream</div>
            </div>

            <div class="divTableCell" id="135">
                <div class="framenr">135</div>
                <div class="kanji">州</div>
                <div class="keyword" style="display: none">state</div>
            </div>

            <div class="divTableCell" id="136">
                <div class="framenr">136</div>
                <div class="kanji">順</div>
                <div class="keyword" style="display: none">obey</div>
            </div>

            <div class="divTableCell" id="137">
                <div class="framenr">137</div>
                <div class="kanji">水</div>
                <div class="keyword" style="display: none">water</div>
            </div>

            <div class="divTableCell" id="138">
                <div class="framenr">138</div>
                <div class="kanji">氷</div>
                <div class="keyword" style="display: none">icicle</div>
            </div>

            <div class="divTableCell" id="139">
                <div class="framenr">139</div>
                <div class="kanji">永</div>
                <div class="keyword" style="display: none">eternity</div>
            </div>

            <div class="divTableCell" id="140">
                <div class="framenr">140</div>
                <div class="kanji">泉</div>
                <div class="keyword" style="display: none">spring</div>
            </div>

            <div class="divTableCell" id="141">
                <div class="framenr">141</div>
                <div class="kanji">腺</div>
                <div class="keyword" style="display: none">gland</div>
            </div>

            <div class="divTableCell" id="142">
                <div class="framenr">142</div>
                <div class="kanji">原</div>
                <div class="keyword" style="display: none">meadow</div>
            </div>

            <div class="divTableCell" id="143">
                <div class="framenr">143</div>
                <div class="kanji">願</div>
                <div class="keyword" style="display: none">petition</div>
            </div>

            <div class="divTableCell" id="144">
                <div class="framenr">144</div>
                <div class="kanji">泳</div>
                <div class="keyword" style="display: none">swim</div>
            </div>

            <div class="divTableCell" id="145">
                <div class="framenr">145</div>
                <div class="kanji">沼</div>
                <div class="keyword" style="display: none">marsh</div>
            </div>

            <div class="divTableCell" id="146">
                <div class="framenr">146</div>
                <div class="kanji">沖</div>
                <div class="keyword" style="display: none">open sea</div>
            </div>

            <div class="divTableCell" id="147">
                <div class="framenr">147</div>
                <div class="kanji">汎</div>
                <div class="keyword" style="display: none">pan-</div>
            </div>

            <div class="divTableCell" id="148">
                <div class="framenr">148</div>
                <div class="kanji">江</div>
                <div class="keyword" style="display: none">creek</div>
            </div>

            <div class="divTableCell" id="149">
                <div class="framenr">149</div>
                <div class="kanji">汰</div>
                <div class="keyword" style="display: none">cleanse(selection)</div>
            </div>

            <div class="divTableCell" id="150">
                <div class="framenr">150</div>
                <div class="kanji">汁</div>
                <div class="keyword" style="display: none">soup</div>
            </div>

            <div class="divTableCell" id="151">
                <div class="framenr">151</div>
                <div class="kanji">沙</div>
                <div class="keyword" style="display: none">grains of sand</div>
            </div>

            <div class="divTableCell" id="152">
                <div class="framenr">152</div>
                <div class="kanji">潮</div>
                <div class="keyword" style="display: none">tide</div>
            </div>

            <div class="divTableCell" id="153">
                <div class="framenr">153</div>
                <div class="kanji">源</div>
                <div class="keyword" style="display: none">source</div>
            </div>

            <div class="divTableCell" id="154">
                <div class="framenr">154</div>
                <div class="kanji">活</div>
                <div class="keyword" style="display: none">lively</div>
            </div>

            <div class="divTableCell" id="155">
                <div class="framenr">155</div>
                <div class="kanji">消</div>
                <div class="keyword" style="display: none">extinguish</div>
            </div>

            <div class="divTableCell" id="156">
                <div class="framenr">156</div>
                <div class="kanji">況</div>
                <div class="keyword" style="display: none">but of course</div>
            </div>

            <div class="divTableCell" id="157">
                <div class="framenr">157</div>
                <div class="kanji">河</div>
                <div class="keyword" style="display: none">river</div>
            </div>

            <div class="divTableCell" id="158">
                <div class="framenr">158</div>
                <div class="kanji">泊</div>
                <div class="keyword" style="display: none">overnight</div>
            </div>

            <div class="divTableCell" id="159">
                <div class="framenr">159</div>
                <div class="kanji">湖</div>
                <div class="keyword" style="display: none">lake</div>
            </div>

            <div class="divTableCell" id="160">
                <div class="framenr">160</div>
                <div class="kanji">測</div>
                <div class="keyword" style="display: none">fathom</div>
            </div>

            <div class="divTableCell" id="161">
                <div class="framenr">161</div>
                <div class="kanji">土</div>
                <div class="keyword" style="display: none">soil</div>
            </div>

            <div class="divTableCell" id="162">
                <div class="framenr">162</div>
                <div class="kanji">吐</div>
                <div class="keyword" style="display: none">spit</div>
            </div>

            <div class="divTableCell" id="163">
                <div class="framenr">163</div>
                <div class="kanji">圧</div>
                <div class="keyword" style="display: none">pressure</div>
            </div>

            <div class="divTableCell" id="164">
                <div class="framenr">164</div>
                <div class="kanji">埼</div>
                <div class="keyword" style="display: none">cape</div>
            </div>

            <div class="divTableCell" id="165">
                <div class="framenr">165</div>
                <div class="kanji">垣</div>
                <div class="keyword" style="display: none">hedge</div>
            </div>

            <div class="divTableCell" id="166">
                <div class="framenr">166</div>
                <div class="kanji">填</div>
                <div class="keyword" style="display: none">inlay(fill in)</div>
            </div>

            <div class="divTableCell" id="167">
                <div class="framenr">167</div>
                <div class="kanji">圭</div>
                <div class="keyword" style="display: none">squared jewel</div>
            </div>

            <div class="divTableCell" id="168">
                <div class="framenr">168</div>
                <div class="kanji">封</div>
                <div class="keyword" style="display: none">seal</div>
            </div>

            <div class="divTableCell" id="169">
                <div class="framenr">169</div>
                <div class="kanji">涯</div>
                <div class="keyword" style="display: none">horizon</div>
            </div>

            <div class="divTableCell" id="170">
                <div class="framenr">170</div>
                <div class="kanji">寺</div>
                <div class="keyword" style="display: none">Buddhist temple</div>
            </div>

            <div class="divTableCell" id="171">
                <div class="framenr">171</div>
                <div class="kanji">時</div>
                <div class="keyword" style="display: none">time</div>
            </div>

            <div class="divTableCell" id="172">
                <div class="framenr">172</div>
                <div class="kanji">均</div>
                <div class="keyword" style="display: none">level</div>
            </div>

            <div class="divTableCell" id="173">
                <div class="framenr">173</div>
                <div class="kanji">火</div>
                <div class="keyword" style="display: none">fire</div>
            </div>

            <div class="divTableCell" id="174">
                <div class="framenr">174</div>
                <div class="kanji">炎</div>
                <div class="keyword" style="display: none">inflammation</div>
            </div>

            <div class="divTableCell" id="175">
                <div class="framenr">175</div>
                <div class="kanji">煩</div>
                <div class="keyword" style="display: none">anxiety</div>
            </div>

            <div class="divTableCell" id="176">
                <div class="framenr">176</div>
                <div class="kanji">淡</div>
                <div class="keyword" style="display: none">thin</div>
            </div>

            <div class="divTableCell" id="177">
                <div class="framenr">177</div>
                <div class="kanji">灯</div>
                <div class="keyword" style="display: none">lamp</div>
            </div>

            <div class="divTableCell" id="178">
                <div class="framenr">178</div>
                <div class="kanji">畑</div>
                <div class="keyword" style="display: none">farm</div>
            </div>

            <div class="divTableCell" id="179">
                <div class="framenr">179</div>
                <div class="kanji">災</div>
                <div class="keyword" style="display: none">disaster</div>
            </div>

            <div class="divTableCell" id="180">
                <div class="framenr">180</div>
                <div class="kanji">灰</div>
                <div class="keyword" style="display: none">ashes</div>
            </div>

            <div class="divTableCell" id="181">
                <div class="framenr">181</div>
                <div class="kanji">点</div>
                <div class="keyword" style="display: none">spot</div>
            </div>

            <div class="divTableCell" id="182">
                <div class="framenr">182</div>
                <div class="kanji">照</div>
                <div class="keyword" style="display: none">illuminate</div>
            </div>

            <div class="divTableCell" id="183">
                <div class="framenr">183</div>
                <div class="kanji">魚</div>
                <div class="keyword" style="display: none">fish</div>
            </div>

            <div class="divTableCell" id="184">
                <div class="framenr">184</div>
                <div class="kanji">漁</div>
                <div class="keyword" style="display: none">fishing</div>
            </div>

            <div class="divTableCell" id="185">
                <div class="framenr">185</div>
                <div class="kanji">里</div>
                <div class="keyword" style="display: none">ri</div>
            </div>

            <div class="divTableCell" id="186">
                <div class="framenr">186</div>
                <div class="kanji">黒</div>
                <div class="keyword" style="display: none">black</div>
            </div>

            <div class="divTableCell" id="187">
                <div class="framenr">187</div>
                <div class="kanji">墨</div>
                <div class="keyword" style="display: none">black ink</div>
            </div>

            <div class="divTableCell" id="188">
                <div class="framenr">188</div>
                <div class="kanji">鯉</div>
                <div class="keyword" style="display: none">carp</div>
            </div>

            <div class="divTableCell" id="189">
                <div class="framenr">189</div>
                <div class="kanji">量</div>
                <div class="keyword" style="display: none">quantity</div>
            </div>

            <div class="divTableCell" id="190">
                <div class="framenr">190</div>
                <div class="kanji">厘</div>
                <div class="keyword" style="display: none">rin</div>
            </div>

            <div class="divTableCell" id="191">
                <div class="framenr">191</div>
                <div class="kanji">埋</div>
                <div class="keyword" style="display: none">bury</div>
            </div>

            <div class="divTableCell" id="192">
                <div class="framenr">192</div>
                <div class="kanji">同</div>
                <div class="keyword" style="display: none">same</div>
            </div>

            <div class="divTableCell" id="193">
                <div class="framenr">193</div>
                <div class="kanji">洞</div>
                <div class="keyword" style="display: none">den</div>
            </div>

            <div class="divTableCell" id="194">
                <div class="framenr">194</div>
                <div class="kanji">胴</div>
                <div class="keyword" style="display: none">trunk</div>
            </div>

            <div class="divTableCell" id="195">
                <div class="framenr">195</div>
                <div class="kanji">向</div>
                <div class="keyword" style="display: none">yonder</div>
            </div>

            <div class="divTableCell" id="196">
                <div class="framenr">196</div>
                <div class="kanji">尚</div>
                <div class="keyword" style="display: none">esteem</div>
            </div>

            <div class="divTableCell" id="197">
                <div class="framenr">197</div>
                <div class="kanji">字</div>
                <div class="keyword" style="display: none">character</div>
            </div>

            <div class="divTableCell" id="198">
                <div class="framenr">198</div>
                <div class="kanji">守</div>
                <div class="keyword" style="display: none">guard</div>
            </div>

            <div class="divTableCell" id="199">
                <div class="framenr">199</div>
                <div class="kanji">完</div>
                <div class="keyword" style="display: none">perfect</div>
            </div>

            <div class="divTableCell" id="200">
                <div class="framenr">200</div>
                <div class="kanji">宣</div>
                <div class="keyword" style="display: none">proclaim</div>
            </div>

            <div class="divTableCell" id="201">
                <div class="framenr">201</div>
                <div class="kanji">宵</div>
                <div class="keyword" style="display: none">wee hours</div>
            </div>

            <div class="divTableCell" id="202">
                <div class="framenr">202</div>
                <div class="kanji">安</div>
                <div class="keyword" style="display: none">relax/cheap</div>
            </div>

            <div class="divTableCell" id="203">
                <div class="framenr">203</div>
                <div class="kanji">宴</div>
                <div class="keyword" style="display: none">banquet</div>
            </div>

            <div class="divTableCell" id="204">
                <div class="framenr">204</div>
                <div class="kanji">寄</div>
                <div class="keyword" style="display: none">draw near</div>
            </div>

            <div class="divTableCell" id="205">
                <div class="framenr">205</div>
                <div class="kanji">富</div>
                <div class="keyword" style="display: none">wealth</div>
            </div>

            <div class="divTableCell" id="206">
                <div class="framenr">206</div>
                <div class="kanji">貯</div>
                <div class="keyword" style="display: none">savings</div>
            </div>

            <div class="divTableCell" id="207">
                <div class="framenr">207</div>
                <div class="kanji">木</div>
                <div class="keyword" style="display: none">tree</div>
            </div>

            <div class="divTableCell" id="208">
                <div class="framenr">208</div>
                <div class="kanji">林</div>
                <div class="keyword" style="display: none">grove</div>
            </div>

            <div class="divTableCell" id="209">
                <div class="framenr">209</div>
                <div class="kanji">森</div>
                <div class="keyword" style="display: none">forest</div>
            </div>

            <div class="divTableCell" id="210">
                <div class="framenr">210</div>
                <div class="kanji">桂</div>
                <div class="keyword" style="display: none">Japanese Judas-tree</div>
            </div>

            <div class="divTableCell" id="211">
                <div class="framenr">211</div>
                <div class="kanji">柏</div>
                <div class="keyword" style="display: none">oak</div>
            </div>

            <div class="divTableCell" id="212">
                <div class="framenr">212</div>
                <div class="kanji">枠</div>
                <div class="keyword" style="display: none">frame</div>
            </div>

            <div class="divTableCell" id="213">
                <div class="framenr">213</div>
                <div class="kanji">梢</div>
                <div class="keyword" style="display: none">treetops</div>
            </div>

            <div class="divTableCell" id="214">
                <div class="framenr">214</div>
                <div class="kanji">棚</div>
                <div class="keyword" style="display: none">shelf</div>
            </div>

            <div class="divTableCell" id="215">
                <div class="framenr">215</div>
                <div class="kanji">杏</div>
                <div class="keyword" style="display: none">apricot</div>
            </div>

            <div class="divTableCell" id="216">
                <div class="framenr">216</div>
                <div class="kanji">桐</div>
                <div class="keyword" style="display: none">paulownia</div>
            </div>

            <div class="divTableCell" id="217">
                <div class="framenr">217</div>
                <div class="kanji">植</div>
                <div class="keyword" style="display: none">plant</div>
            </div>

            <div class="divTableCell" id="218">
                <div class="framenr">218</div>
                <div class="kanji">椅</div>
                <div class="keyword" style="display: none">chair</div>
            </div>

            <div class="divTableCell" id="219">
                <div class="framenr">219</div>
                <div class="kanji">枯</div>
                <div class="keyword" style="display: none">wither</div>
            </div>

            <div class="divTableCell" id="220">
                <div class="framenr">220</div>
                <div class="kanji">朴</div>
                <div class="keyword" style="display: none">crude</div>
            </div>

            <div class="divTableCell" id="221">
                <div class="framenr">221</div>
                <div class="kanji">村</div>
                <div class="keyword" style="display: none">village</div>
            </div>

            <div class="divTableCell" id="222">
                <div class="framenr">222</div>
                <div class="kanji">相</div>
                <div class="keyword" style="display: none">inter-</div>
            </div>

            <div class="divTableCell" id="223">
                <div class="framenr">223</div>
                <div class="kanji">机</div>
                <div class="keyword" style="display: none">desk</div>
            </div>

            <div class="divTableCell" id="224">
                <div class="framenr">224</div>
                <div class="kanji">本</div>
                <div class="keyword" style="display: none">book</div>
            </div>

            <div class="divTableCell" id="225">
                <div class="framenr">225</div>
                <div class="kanji">札</div>
                <div class="keyword" style="display: none">tag</div>
            </div>

            <div class="divTableCell" id="226">
                <div class="framenr">226</div>
                <div class="kanji">暦</div>
                <div class="keyword" style="display: none">calendar</div>
            </div>

            <div class="divTableCell" id="227">
                <div class="framenr">227</div>
                <div class="kanji">案</div>
                <div class="keyword" style="display: none">plan</div>
            </div>

            <div class="divTableCell" id="228">
                <div class="framenr">228</div>
                <div class="kanji">燥</div>
                <div class="keyword" style="display: none">parch</div>
            </div>

            <div class="divTableCell" id="229">
                <div class="framenr">229</div>
                <div class="kanji">未</div>
                <div class="keyword" style="display: none">not yet</div>
            </div>

            <div class="divTableCell" id="230">
                <div class="framenr">230</div>
                <div class="kanji">末</div>
                <div class="keyword" style="display: none">extremity</div>
            </div>

            <div class="divTableCell" id="231">
                <div class="framenr">231</div>
                <div class="kanji">昧</div>
                <div class="keyword" style="display: none">obscure</div>
            </div>

            <div class="divTableCell" id="232">
                <div class="framenr">232</div>
                <div class="kanji">沫</div>
                <div class="keyword" style="display: none">splash</div>
            </div>

            <div class="divTableCell" id="233">
                <div class="framenr">233</div>
                <div class="kanji">味</div>
                <div class="keyword" style="display: none">flavor</div>
            </div>

            <div class="divTableCell" id="234">
                <div class="framenr">234</div>
                <div class="kanji">妹</div>
                <div class="keyword" style="display: none">younger sister</div>
            </div>

            <div class="divTableCell" id="235">
                <div class="framenr">235</div>
                <div class="kanji">朱</div>
                <div class="keyword" style="display: none">vermilion</div>
            </div>

            <div class="divTableCell" id="236">
                <div class="framenr">236</div>
                <div class="kanji">株</div>
                <div class="keyword" style="display: none">stocks</div>
            </div>

            <div class="divTableCell" id="237">
                <div class="framenr">237</div>
                <div class="kanji">若</div>
                <div class="keyword" style="display: none">young</div>
            </div>

            <div class="divTableCell" id="238">
                <div class="framenr">238</div>
                <div class="kanji">草</div>
                <div class="keyword" style="display: none">grass</div>
            </div>

            <div class="divTableCell" id="239">
                <div class="framenr">239</div>
                <div class="kanji">苦</div>
                <div class="keyword" style="display: none">suffering</div>
            </div>

            <div class="divTableCell" id="240">
                <div class="framenr">240</div>
                <div class="kanji">苛</div>
                <div class="keyword" style="display: none">bullying</div>
            </div>

            <div class="divTableCell" id="241">
                <div class="framenr">241</div>
                <div class="kanji">寛</div>
                <div class="keyword" style="display: none">tolerant</div>
            </div>

            <div class="divTableCell" id="242">
                <div class="framenr">242</div>
                <div class="kanji">薄</div>
                <div class="keyword" style="display: none">dilute</div>
            </div>

            <div class="divTableCell" id="243">
                <div class="framenr">243</div>
                <div class="kanji">葉</div>
                <div class="keyword" style="display: none">leaf</div>
            </div>

            <div class="divTableCell" id="244">
                <div class="framenr">244</div>
                <div class="kanji">模</div>
                <div class="keyword" style="display: none">imitation</div>
            </div>

            <div class="divTableCell" id="245">
                <div class="framenr">245</div>
                <div class="kanji">漠</div>
                <div class="keyword" style="display: none">vague</div>
            </div>

            <div class="divTableCell" id="246">
                <div class="framenr">246</div>
                <div class="kanji">墓</div>
                <div class="keyword" style="display: none">grave</div>
            </div>

            <div class="divTableCell" id="247">
                <div class="framenr">247</div>
                <div class="kanji">暮</div>
                <div class="keyword" style="display: none">livelihood</div>
            </div>

            <div class="divTableCell" id="248">
                <div class="framenr">248</div>
                <div class="kanji">膜</div>
                <div class="keyword" style="display: none">membrane</div>
            </div>

            <div class="divTableCell" id="249">
                <div class="framenr">249</div>
                <div class="kanji">苗</div>
                <div class="keyword" style="display: none">seedling</div>
            </div>

            <div class="divTableCell" id="250">
                <div class="framenr">250</div>
                <div class="kanji">兆</div>
                <div class="keyword" style="display: none">portent</div>
            </div>

            <div class="divTableCell" id="251">
                <div class="framenr">251</div>
                <div class="kanji">桃</div>
                <div class="keyword" style="display: none">peach tree</div>
            </div>

            <div class="divTableCell" id="252">
                <div class="framenr">252</div>
                <div class="kanji">眺</div>
                <div class="keyword" style="display: none">stare</div>
            </div>

            <div class="divTableCell" id="253">
                <div class="framenr">253</div>
                <div class="kanji">犬</div>
                <div class="keyword" style="display: none">dog</div>
            </div>

            <div class="divTableCell" id="254">
                <div class="framenr">254</div>
                <div class="kanji">状</div>
                <div class="keyword" style="display: none">status quo</div>
            </div>

            <div class="divTableCell" id="255">
                <div class="framenr">255</div>
                <div class="kanji">黙</div>
                <div class="keyword" style="display: none">silence</div>
            </div>

            <div class="divTableCell" id="256">
                <div class="framenr">256</div>
                <div class="kanji">然</div>
                <div class="keyword" style="display: none">sort of thing</div>
            </div>

            <div class="divTableCell" id="257">
                <div class="framenr">257</div>
                <div class="kanji">荻</div>
                <div class="keyword" style="display: none">reed</div>
            </div>

            <div class="divTableCell" id="258">
                <div class="framenr">258</div>
                <div class="kanji">狩</div>
                <div class="keyword" style="display: none">hunt</div>
            </div>

            <div class="divTableCell" id="259">
                <div class="framenr">259</div>
                <div class="kanji">猫</div>
                <div class="keyword" style="display: none">cat</div>
            </div>

            <div class="divTableCell" id="260">
                <div class="framenr">260</div>
                <div class="kanji">牛</div>
                <div class="keyword" style="display: none">cow</div>
            </div>

            <div class="divTableCell" id="261">
                <div class="framenr">261</div>
                <div class="kanji">特</div>
                <div class="keyword" style="display: none">special</div>
            </div>

            <div class="divTableCell" id="262">
                <div class="framenr">262</div>
                <div class="kanji">告</div>
                <div class="keyword" style="display: none">revelation</div>
            </div>

            <div class="divTableCell" id="263">
                <div class="framenr">263</div>
                <div class="kanji">先</div>
                <div class="keyword" style="display: none">before</div>
            </div>

            <div class="divTableCell" id="264">
                <div class="framenr">264</div>
                <div class="kanji">洗</div>
                <div class="keyword" style="display: none">wash</div>
            </div>

            <div class="divTableCell" id="265">
                <div class="framenr">265</div>
                <div class="kanji">介</div>
                <div class="keyword" style="display: none">jammed in</div>
            </div>

            <div class="divTableCell" id="266">
                <div class="framenr">266</div>
                <div class="kanji">界</div>
                <div class="keyword" style="display: none">world</div>
            </div>

            <div class="divTableCell" id="267">
                <div class="framenr">267</div>
                <div class="kanji">茶</div>
                <div class="keyword" style="display: none">tea</div>
            </div>

            <div class="divTableCell" id="268">
                <div class="framenr">268</div>
                <div class="kanji">脊</div>
                <div class="keyword" style="display: none">spinal column</div>
            </div>

            <div class="divTableCell" id="269">
                <div class="framenr">269</div>
                <div class="kanji">合</div>
                <div class="keyword" style="display: none">fit</div>
            </div>

            <div class="divTableCell" id="270">
                <div class="framenr">270</div>
                <div class="kanji">塔</div>
                <div class="keyword" style="display: none">pagoda</div>
            </div>

            <div class="divTableCell" id="271">
                <div class="framenr">271</div>
                <div class="kanji">王</div>
                <div class="keyword" style="display: none">king</div>
            </div>

            <div class="divTableCell" id="272">
                <div class="framenr">272</div>
                <div class="kanji">玉</div>
                <div class="keyword" style="display: none">jewel</div>
            </div>

            <div class="divTableCell" id="273">
                <div class="framenr">273</div>
                <div class="kanji">宝</div>
                <div class="keyword" style="display: none">treasure</div>
            </div>

            <div class="divTableCell" id="274">
                <div class="framenr">274</div>
                <div class="kanji">珠</div>
                <div class="keyword" style="display: none">pearl</div>
            </div>

            <div class="divTableCell" id="275">
                <div class="framenr">275</div>
                <div class="kanji">現</div>
                <div class="keyword" style="display: none">present</div>
            </div>

            <div class="divTableCell" id="276">
                <div class="framenr">276</div>
                <div class="kanji">玩</div>
                <div class="keyword" style="display: none">toy</div>
            </div>

            <div class="divTableCell" id="277">
                <div class="framenr">277</div>
                <div class="kanji">狂</div>
                <div class="keyword" style="display: none">lunatic</div>
            </div>

            <div class="divTableCell" id="278">
                <div class="framenr">278</div>
                <div class="kanji">旺</div>
                <div class="keyword" style="display: none">effulgent</div>
            </div>

            <div class="divTableCell" id="279">
                <div class="framenr">279</div>
                <div class="kanji">皇</div>
                <div class="keyword" style="display: none">emperor</div>
            </div>

            <div class="divTableCell" id="280">
                <div class="framenr">280</div>
                <div class="kanji">呈</div>
                <div class="keyword" style="display: none">display</div>
            </div>

            <div class="divTableCell" id="281">
                <div class="framenr">281</div>
                <div class="kanji">全</div>
                <div class="keyword" style="display: none">whole</div>
            </div>

            <div class="divTableCell" id="282">
                <div class="framenr">282</div>
                <div class="kanji">栓</div>
                <div class="keyword" style="display: none">plug</div>
            </div>

            <div class="divTableCell" id="283">
                <div class="framenr">283</div>
                <div class="kanji">理</div>
                <div class="keyword" style="display: none">logic</div>
            </div>

            <div class="divTableCell" id="284">
                <div class="framenr">284</div>
                <div class="kanji">主</div>
                <div class="keyword" style="display: none">lord</div>
            </div>

            <div class="divTableCell" id="285">
                <div class="framenr">285</div>
                <div class="kanji">注</div>
                <div class="keyword" style="display: none">pour</div>
            </div>

            <div class="divTableCell" id="286">
                <div class="framenr">286</div>
                <div class="kanji">柱</div>
                <div class="keyword" style="display: none">pillar</div>
            </div>

            <div class="divTableCell" id="287">
                <div class="framenr">287</div>
                <div class="kanji">金</div>
                <div class="keyword" style="display: none">gold</div>
            </div>

            <div class="divTableCell" id="288">
                <div class="framenr">288</div>
                <div class="kanji">銑</div>
                <div class="keyword" style="display: none">pig iron</div>
            </div>

            <div class="divTableCell" id="289">
                <div class="framenr">289</div>
                <div class="kanji">鉢</div>
                <div class="keyword" style="display: none">bowl</div>
            </div>

            <div class="divTableCell" id="290">
                <div class="framenr">290</div>
                <div class="kanji">銅</div>
                <div class="keyword" style="display: none">copper</div>
            </div>

            <div class="divTableCell" id="291">
                <div class="framenr">291</div>
                <div class="kanji">釣</div>
                <div class="keyword" style="display: none">angling</div>
            </div>

            <div class="divTableCell" id="292">
                <div class="framenr">292</div>
                <div class="kanji">針</div>
                <div class="keyword" style="display: none">needle</div>
            </div>

            <div class="divTableCell" id="293">
                <div class="framenr">293</div>
                <div class="kanji">銘</div>
                <div class="keyword" style="display: none">inscription</div>
            </div>

            <div class="divTableCell" id="294">
                <div class="framenr">294</div>
                <div class="kanji">鎮</div>
                <div class="keyword" style="display: none">tranquilize</div>
            </div>

            <div class="divTableCell" id="295">
                <div class="framenr">295</div>
                <div class="kanji">道</div>
                <div class="keyword" style="display: none">road-way</div>
            </div>

            <div class="divTableCell" id="296">
                <div class="framenr">296</div>
                <div class="kanji">導</div>
                <div class="keyword" style="display: none">guidance</div>
            </div>

            <div class="divTableCell" id="297">
                <div class="framenr">297</div>
                <div class="kanji">辻</div>
                <div class="keyword" style="display: none">crossing</div>
            </div>

            <div class="divTableCell" id="298">
                <div class="framenr">298</div>
                <div class="kanji">迅</div>
                <div class="keyword" style="display: none">swift</div>
            </div>

            <div class="divTableCell" id="299">
                <div class="framenr">299</div>
                <div class="kanji">造</div>
                <div class="keyword" style="display: none">create</div>
            </div>

            <div class="divTableCell" id="300">
                <div class="framenr">300</div>
                <div class="kanji">迫</div>
                <div class="keyword" style="display: none">urge</div>
            </div>

            <div class="divTableCell" id="301">
                <div class="framenr">301</div>
                <div class="kanji">逃</div>
                <div class="keyword" style="display: none">escape</div>
            </div>

            <div class="divTableCell" id="302">
                <div class="framenr">302</div>
                <div class="kanji">辺</div>
                <div class="keyword" style="display: none">environs</div>
            </div>

            <div class="divTableCell" id="303">
                <div class="framenr">303</div>
                <div class="kanji">巡</div>
                <div class="keyword" style="display: none">patrol</div>
            </div>

            <div class="divTableCell" id="304">
                <div class="framenr">304</div>
                <div class="kanji">車</div>
                <div class="keyword" style="display: none">car</div>
            </div>

            <div class="divTableCell" id="305">
                <div class="framenr">305</div>
                <div class="kanji">連</div>
                <div class="keyword" style="display: none">take along</div>
            </div>

            <div class="divTableCell" id="306">
                <div class="framenr">306</div>
                <div class="kanji">軌</div>
                <div class="keyword" style="display: none">rut</div>
            </div>

            <div class="divTableCell" id="307">
                <div class="framenr">307</div>
                <div class="kanji">輸</div>
                <div class="keyword" style="display: none">transport</div>
            </div>

            <div class="divTableCell" id="308">
                <div class="framenr">308</div>
                <div class="kanji">喩</div>
                <div class="keyword" style="display: none">metaphor</div>
            </div>

            <div class="divTableCell" id="309">
                <div class="framenr">309</div>
                <div class="kanji">前</div>
                <div class="keyword" style="display: none">in front</div>
            </div>

            <div class="divTableCell" id="310">
                <div class="framenr">310</div>
                <div class="kanji">煎</div>
                <div class="keyword" style="display: none">roast</div>
            </div>

            <div class="divTableCell" id="311">
                <div class="framenr">311</div>
                <div class="kanji">各</div>
                <div class="keyword" style="display: none">each</div>
            </div>

            <div class="divTableCell" id="312">
                <div class="framenr">312</div>
                <div class="kanji">格</div>
                <div class="keyword" style="display: none">status</div>
            </div>

            <div class="divTableCell" id="313">
                <div class="framenr">313</div>
                <div class="kanji">賂</div>
                <div class="keyword" style="display: none">graft</div>
            </div>

            <div class="divTableCell" id="314">
                <div class="framenr">314</div>
                <div class="kanji">略</div>
                <div class="keyword" style="display: none">abbreviation</div>
            </div>

            <div class="divTableCell" id="315">
                <div class="framenr">315</div>
                <div class="kanji">客</div>
                <div class="keyword" style="display: none">guest</div>
            </div>

            <div class="divTableCell" id="316">
                <div class="framenr">316</div>
                <div class="kanji">額</div>
                <div class="keyword" style="display: none">forehead</div>
            </div>

            <div class="divTableCell" id="317">
                <div class="framenr">317</div>
                <div class="kanji">夏</div>
                <div class="keyword" style="display: none">summer</div>
            </div>

            <div class="divTableCell" id="318">
                <div class="framenr">318</div>
                <div class="kanji">処</div>
                <div class="keyword" style="display: none">dispose</div>
            </div>

            <div class="divTableCell" id="319">
                <div class="framenr">319</div>
                <div class="kanji">条</div>
                <div class="keyword" style="display: none">twig</div>
            </div>

            <div class="divTableCell" id="320">
                <div class="framenr">320</div>
                <div class="kanji">落</div>
                <div class="keyword" style="display: none">fall</div>
            </div>

            <div class="divTableCell" id="321">
                <div class="framenr">321</div>
                <div class="kanji">冗</div>
                <div class="keyword" style="display: none">superfluous</div>
            </div>

            <div class="divTableCell" id="322">
                <div class="framenr">322</div>
                <div class="kanji">冥</div>
                <div class="keyword" style="display: none">Hades</div>
            </div>

            <div class="divTableCell" id="323">
                <div class="framenr">323</div>
                <div class="kanji">軍</div>
                <div class="keyword" style="display: none">army</div>
            </div>

            <div class="divTableCell" id="324">
                <div class="framenr">324</div>
                <div class="kanji">輝</div>
                <div class="keyword" style="display: none">radiance</div>
            </div>

            <div class="divTableCell" id="325">
                <div class="framenr">325</div>
                <div class="kanji">運</div>
                <div class="keyword" style="display: none">carry</div>
            </div>

            <div class="divTableCell" id="326">
                <div class="framenr">326</div>
                <div class="kanji">冠</div>
                <div class="keyword" style="display: none">crown</div>
            </div>

            <div class="divTableCell" id="327">
                <div class="framenr">327</div>
                <div class="kanji">夢</div>
                <div class="keyword" style="display: none">dream</div>
            </div>

            <div class="divTableCell" id="328">
                <div class="framenr">328</div>
                <div class="kanji">坑</div>
                <div class="keyword" style="display: none">pit</div>
            </div>

            <div class="divTableCell" id="329">
                <div class="framenr">329</div>
                <div class="kanji">高</div>
                <div class="keyword" style="display: none">tall</div>
            </div>

            <div class="divTableCell" id="330">
                <div class="framenr">330</div>
                <div class="kanji">享</div>
                <div class="keyword" style="display: none">receive</div>
            </div>

            <div class="divTableCell" id="331">
                <div class="framenr">331</div>
                <div class="kanji">塾</div>
                <div class="keyword" style="display: none">cram school</div>
            </div>

            <div class="divTableCell" id="332">
                <div class="framenr">332</div>
                <div class="kanji">熟</div>
                <div class="keyword" style="display: none">mellow</div>
            </div>

            <div class="divTableCell" id="333">
                <div class="framenr">333</div>
                <div class="kanji">亭</div>
                <div class="keyword" style="display: none">pavilion</div>
            </div>

            <div class="divTableCell" id="334">
                <div class="framenr">334</div>
                <div class="kanji">京</div>
                <div class="keyword" style="display: none">capital</div>
            </div>

            <div class="divTableCell" id="335">
                <div class="framenr">335</div>
                <div class="kanji">涼</div>
                <div class="keyword" style="display: none">refreshing</div>
            </div>

            <div class="divTableCell" id="336">
                <div class="framenr">336</div>
                <div class="kanji">景</div>
                <div class="keyword" style="display: none">scenery</div>
            </div>

            <div class="divTableCell" id="337">
                <div class="framenr">337</div>
                <div class="kanji">鯨</div>
                <div class="keyword" style="display: none">whale</div>
            </div>

            <div class="divTableCell" id="338">
                <div class="framenr">338</div>
                <div class="kanji">舎</div>
                <div class="keyword" style="display: none">cottage</div>
            </div>

            <div class="divTableCell" id="339">
                <div class="framenr">339</div>
                <div class="kanji">周</div>
                <div class="keyword" style="display: none">circumference</div>
            </div>

            <div class="divTableCell" id="340">
                <div class="framenr">340</div>
                <div class="kanji">週</div>
                <div class="keyword" style="display: none">week</div>
            </div>

            <div class="divTableCell" id="341">
                <div class="framenr">341</div>
                <div class="kanji">士</div>
                <div class="keyword" style="display: none">gentleman</div>
            </div>

            <div class="divTableCell" id="342">
                <div class="framenr">342</div>
                <div class="kanji">吉</div>
                <div class="keyword" style="display: none">good luck</div>
            </div>

            <div class="divTableCell" id="343">
                <div class="framenr">343</div>
                <div class="kanji">壮</div>
                <div class="keyword" style="display: none">robust</div>
            </div>

            <div class="divTableCell" id="344">
                <div class="framenr">344</div>
                <div class="kanji">荘</div>
                <div class="keyword" style="display: none">villa</div>
            </div>

            <div class="divTableCell" id="345">
                <div class="framenr">345</div>
                <div class="kanji">売</div>
                <div class="keyword" style="display: none">sell</div>
            </div>

            <div class="divTableCell" id="346">
                <div class="framenr">346</div>
                <div class="kanji">学</div>
                <div class="keyword" style="display: none">study</div>
            </div>

            <div class="divTableCell" id="347">
                <div class="framenr">347</div>
                <div class="kanji">覚</div>
                <div class="keyword" style="display: none">memorize</div>
            </div>

            <div class="divTableCell" id="348">
                <div class="framenr">348</div>
                <div class="kanji">栄</div>
                <div class="keyword" style="display: none">flourish</div>
            </div>

            <div class="divTableCell" id="349">
                <div class="framenr">349</div>
                <div class="kanji">書</div>
                <div class="keyword" style="display: none">write</div>
            </div>

            <div class="divTableCell" id="350">
                <div class="framenr">350</div>
                <div class="kanji">津</div>
                <div class="keyword" style="display: none">haven</div>
            </div>

            <div class="divTableCell" id="351">
                <div class="framenr">351</div>
                <div class="kanji">牧</div>
                <div class="keyword" style="display: none">breed</div>
            </div>

            <div class="divTableCell" id="352">
                <div class="framenr">352</div>
                <div class="kanji">攻</div>
                <div class="keyword" style="display: none">aggression</div>
            </div>

            <div class="divTableCell" id="353">
                <div class="framenr">353</div>
                <div class="kanji">敗</div>
                <div class="keyword" style="display: none">failure</div>
            </div>

            <div class="divTableCell" id="354">
                <div class="framenr">354</div>
                <div class="kanji">枚</div>
                <div class="keyword" style="display: none">a sheet of</div>
            </div>

            <div class="divTableCell" id="355">
                <div class="framenr">355</div>
                <div class="kanji">故</div>
                <div class="keyword" style="display: none">happenstance</div>
            </div>

            <div class="divTableCell" id="356">
                <div class="framenr">356</div>
                <div class="kanji">敬</div>
                <div class="keyword" style="display: none">awe</div>
            </div>

            <div class="divTableCell" id="357">
                <div class="framenr">357</div>
                <div class="kanji">言</div>
                <div class="keyword" style="display: none">say</div>
            </div>

            <div class="divTableCell" id="358">
                <div class="framenr">358</div>
                <div class="kanji">警</div>
                <div class="keyword" style="display: none">admonish</div>
            </div>

            <div class="divTableCell" id="359">
                <div class="framenr">359</div>
                <div class="kanji">計</div>
                <div class="keyword" style="display: none">plot</div>
            </div>

            <div class="divTableCell" id="360">
                <div class="framenr">360</div>
                <div class="kanji">詮</div>
                <div class="keyword" style="display: none">elucidate</div>
            </div>

            <div class="divTableCell" id="361">
                <div class="framenr">361</div>
                <div class="kanji">獄</div>
                <div class="keyword" style="display: none">prison</div>
            </div>

            <div class="divTableCell" id="362">
                <div class="framenr">362</div>
                <div class="kanji">訂</div>
                <div class="keyword" style="display: none">revise</div>
            </div>

            <div class="divTableCell" id="363">
                <div class="framenr">363</div>
                <div class="kanji">訃</div>
                <div class="keyword" style="display: none">obituary</div>
            </div>

            <div class="divTableCell" id="364">
                <div class="framenr">364</div>
                <div class="kanji">討</div>
                <div class="keyword" style="display: none">chastise</div>
            </div>

            <div class="divTableCell" id="365">
                <div class="framenr">365</div>
                <div class="kanji">訓</div>
                <div class="keyword" style="display: none">instruction</div>
            </div>

            <div class="divTableCell" id="366">
                <div class="framenr">366</div>
                <div class="kanji">詔</div>
                <div class="keyword" style="display: none">imperial edict</div>
            </div>

            <div class="divTableCell" id="367">
                <div class="framenr">367</div>
                <div class="kanji">詰</div>
                <div class="keyword" style="display: none">packed</div>
            </div>

            <div class="divTableCell" id="368">
                <div class="framenr">368</div>
                <div class="kanji">話</div>
                <div class="keyword" style="display: none">tale</div>
            </div>

            <div class="divTableCell" id="369">
                <div class="framenr">369</div>
                <div class="kanji">詠</div>
                <div class="keyword" style="display: none">recitation</div>
            </div>

            <div class="divTableCell" id="370">
                <div class="framenr">370</div>
                <div class="kanji">詩</div>
                <div class="keyword" style="display: none">poem</div>
            </div>

            <div class="divTableCell" id="371">
                <div class="framenr">371</div>
                <div class="kanji">語</div>
                <div class="keyword" style="display: none">word</div>
            </div>

            <div class="divTableCell" id="372">
                <div class="framenr">372</div>
                <div class="kanji">読</div>
                <div class="keyword" style="display: none">read</div>
            </div>

            <div class="divTableCell" id="373">
                <div class="framenr">373</div>
                <div class="kanji">調</div>
                <div class="keyword" style="display: none">tune</div>
            </div>

            <div class="divTableCell" id="374">
                <div class="framenr">374</div>
                <div class="kanji">談</div>
                <div class="keyword" style="display: none">discuss</div>
            </div>

            <div class="divTableCell" id="375">
                <div class="framenr">375</div>
                <div class="kanji">諾</div>
                <div class="keyword" style="display: none">consent</div>
            </div>

            <div class="divTableCell" id="376">
                <div class="framenr">376</div>
                <div class="kanji">諭</div>
                <div class="keyword" style="display: none">rebuke</div>
            </div>

            <div class="divTableCell" id="377">
                <div class="framenr">377</div>
                <div class="kanji">式</div>
                <div class="keyword" style="display: none">style</div>
            </div>

            <div class="divTableCell" id="378">
                <div class="framenr">378</div>
                <div class="kanji">試</div>
                <div class="keyword" style="display: none">test</div>
            </div>

            <div class="divTableCell" id="379">
                <div class="framenr">379</div>
                <div class="kanji">弐</div>
                <div class="keyword" style="display: none">II (two)</div>
            </div>

            <div class="divTableCell" id="380">
                <div class="framenr">380</div>
                <div class="kanji">域</div>
                <div class="keyword" style="display: none">range</div>
            </div>

            <div class="divTableCell" id="381">
                <div class="framenr">381</div>
                <div class="kanji">賊</div>
                <div class="keyword" style="display: none">burglar</div>
            </div>

            <div class="divTableCell" id="382">
                <div class="framenr">382</div>
                <div class="kanji">栽</div>
                <div class="keyword" style="display: none">plantation</div>
            </div>

            <div class="divTableCell" id="383">
                <div class="framenr">383</div>
                <div class="kanji">載</div>
                <div class="keyword" style="display: none">load</div>
            </div>

            <div class="divTableCell" id="384">
                <div class="framenr">384</div>
                <div class="kanji">茂</div>
                <div class="keyword" style="display: none">overgrown</div>
            </div>

            <div class="divTableCell" id="385">
                <div class="framenr">385</div>
                <div class="kanji">戚</div>
                <div class="keyword" style="display: none">relatives</div>
            </div>

            <div class="divTableCell" id="386">
                <div class="framenr">386</div>
                <div class="kanji">成</div>
                <div class="keyword" style="display: none">turn into</div>
            </div>

            <div class="divTableCell" id="387">
                <div class="framenr">387</div>
                <div class="kanji">城</div>
                <div class="keyword" style="display: none">castle</div>
            </div>

            <div class="divTableCell" id="388">
                <div class="framenr">388</div>
                <div class="kanji">誠</div>
                <div class="keyword" style="display: none">sincerity</div>
            </div>

            <div class="divTableCell" id="389">
                <div class="framenr">389</div>
                <div class="kanji">威</div>
                <div class="keyword" style="display: none">intimidate</div>
            </div>

            <div class="divTableCell" id="390">
                <div class="framenr">390</div>
                <div class="kanji">滅</div>
                <div class="keyword" style="display: none">destroy</div>
            </div>

            <div class="divTableCell" id="391">
                <div class="framenr">391</div>
                <div class="kanji">減</div>
                <div class="keyword" style="display: none">dwindle</div>
            </div>

            <div class="divTableCell" id="392">
                <div class="framenr">392</div>
                <div class="kanji">蔑</div>
                <div class="keyword" style="display: none">revile</div>
            </div>

            <div class="divTableCell" id="393">
                <div class="framenr">393</div>
                <div class="kanji">桟</div>
                <div class="keyword" style="display: none">scaffold</div>
            </div>

            <div class="divTableCell" id="394">
                <div class="framenr">394</div>
                <div class="kanji">銭</div>
                <div class="keyword" style="display: none">coin</div>
            </div>

            <div class="divTableCell" id="395">
                <div class="framenr">395</div>
                <div class="kanji">浅</div>
                <div class="keyword" style="display: none">shallow</div>
            </div>

            <div class="divTableCell" id="396">
                <div class="framenr">396</div>
                <div class="kanji">止</div>
                <div class="keyword" style="display: none">stop</div>
            </div>

            <div class="divTableCell" id="397">
                <div class="framenr">397</div>
                <div class="kanji">歩</div>
                <div class="keyword" style="display: none">walk</div>
            </div>

            <div class="divTableCell" id="398">
                <div class="framenr">398</div>
                <div class="kanji">渉</div>
                <div class="keyword" style="display: none">ford</div>
            </div>

            <div class="divTableCell" id="399">
                <div class="framenr">399</div>
                <div class="kanji">頻</div>
                <div class="keyword" style="display: none">repeatedly</div>
            </div>

            <div class="divTableCell" id="400">
                <div class="framenr">400</div>
                <div class="kanji">肯</div>
                <div class="keyword" style="display: none">agreement</div>
            </div>

            <div class="divTableCell" id="401">
                <div class="framenr">401</div>
                <div class="kanji">企</div>
                <div class="keyword" style="display: none">undertake</div>
            </div>

            <div class="divTableCell" id="402">
                <div class="framenr">402</div>
                <div class="kanji">歴</div>
                <div class="keyword" style="display: none">curriculum</div>
            </div>

            <div class="divTableCell" id="403">
                <div class="framenr">403</div>
                <div class="kanji">武</div>
                <div class="keyword" style="display: none">warrior</div>
            </div>

            <div class="divTableCell" id="404">
                <div class="framenr">404</div>
                <div class="kanji">賦</div>
                <div class="keyword" style="display: none">levy</div>
            </div>

            <div class="divTableCell" id="405">
                <div class="framenr">405</div>
                <div class="kanji">正</div>
                <div class="keyword" style="display: none">correct</div>
            </div>

            <div class="divTableCell" id="406">
                <div class="framenr">406</div>
                <div class="kanji">証</div>
                <div class="keyword" style="display: none">evidence</div>
            </div>

            <div class="divTableCell" id="407">
                <div class="framenr">407</div>
                <div class="kanji">政</div>
                <div class="keyword" style="display: none">politics</div>
            </div>

            <div class="divTableCell" id="408">
                <div class="framenr">408</div>
                <div class="kanji">定</div>
                <div class="keyword" style="display: none">determine</div>
            </div>

            <div class="divTableCell" id="409">
                <div class="framenr">409</div>
                <div class="kanji">錠</div>
                <div class="keyword" style="display: none">lock</div>
            </div>

            <div class="divTableCell" id="410">
                <div class="framenr">410</div>
                <div class="kanji">走</div>
                <div class="keyword" style="display: none">run</div>
            </div>

            <div class="divTableCell" id="411">
                <div class="framenr">411</div>
                <div class="kanji">超</div>
                <div class="keyword" style="display: none">transcend</div>
            </div>

            <div class="divTableCell" id="412">
                <div class="framenr">412</div>
                <div class="kanji">赴</div>
                <div class="keyword" style="display: none">proceed</div>
            </div>

            <div class="divTableCell" id="413">
                <div class="framenr">413</div>
                <div class="kanji">越</div>
                <div class="keyword" style="display: none">surpass</div>
            </div>

            <div class="divTableCell" id="414">
                <div class="framenr">414</div>
                <div class="kanji">是</div>
                <div class="keyword" style="display: none">just so</div>
            </div>

            <div class="divTableCell" id="415">
                <div class="framenr">415</div>
                <div class="kanji">題</div>
                <div class="keyword" style="display: none">topic</div>
            </div>

            <div class="divTableCell" id="416">
                <div class="framenr">416</div>
                <div class="kanji">堤</div>
                <div class="keyword" style="display: none">dike</div>
            </div>

            <div class="divTableCell" id="417">
                <div class="framenr">417</div>
                <div class="kanji">建</div>
                <div class="keyword" style="display: none">build</div>
            </div>

            <div class="divTableCell" id="418">
                <div class="framenr">418</div>
                <div class="kanji">鍵</div>
                <div class="keyword" style="display: none">key</div>
            </div>

            <div class="divTableCell" id="419">
                <div class="framenr">419</div>
                <div class="kanji">延</div>
                <div class="keyword" style="display: none">prolong</div>
            </div>

            <div class="divTableCell" id="420">
                <div class="framenr">420</div>
                <div class="kanji">誕</div>
                <div class="keyword" style="display: none">nativity</div>
            </div>

            <div class="divTableCell" id="421">
                <div class="framenr">421</div>
                <div class="kanji">礎</div>
                <div class="keyword" style="display: none">cornerstone</div>
            </div>

            <div class="divTableCell" id="422">
                <div class="framenr">422</div>
                <div class="kanji">婿</div>
                <div class="keyword" style="display: none">bridegroom</div>
            </div>

            <div class="divTableCell" id="423">
                <div class="framenr">423</div>
                <div class="kanji">衣</div>
                <div class="keyword" style="display: none">garment</div>
            </div>

            <div class="divTableCell" id="424">
                <div class="framenr">424</div>
                <div class="kanji">裁</div>
                <div class="keyword" style="display: none">tailor</div>
            </div>

            <div class="divTableCell" id="425">
                <div class="framenr">425</div>
                <div class="kanji">装</div>
                <div class="keyword" style="display: none">attire</div>
            </div>

            <div class="divTableCell" id="426">
                <div class="framenr">426</div>
                <div class="kanji">裏</div>
                <div class="keyword" style="display: none">back</div>
            </div>

            <div class="divTableCell" id="427">
                <div class="framenr">427</div>
                <div class="kanji">壊</div>
                <div class="keyword" style="display: none">demolition</div>
            </div>

            <div class="divTableCell" id="428">
                <div class="framenr">428</div>
                <div class="kanji">哀</div>
                <div class="keyword" style="display: none">pathetic</div>
            </div>

            <div class="divTableCell" id="429">
                <div class="framenr">429</div>
                <div class="kanji">遠</div>
                <div class="keyword" style="display: none">distant</div>
            </div>

            <div class="divTableCell" id="430">
                <div class="framenr">430</div>
                <div class="kanji">猿</div>
                <div class="keyword" style="display: none">monkey</div>
            </div>

            <div class="divTableCell" id="431">
                <div class="framenr">431</div>
                <div class="kanji">初</div>
                <div class="keyword" style="display: none">first time</div>
            </div>

            <div class="divTableCell" id="432">
                <div class="framenr">432</div>
                <div class="kanji">巾</div>
                <div class="keyword" style="display: none">towel</div>
            </div>

            <div class="divTableCell" id="433">
                <div class="framenr">433</div>
                <div class="kanji">布</div>
                <div class="keyword" style="display: none">linen</div>
            </div>

            <div class="divTableCell" id="434">
                <div class="framenr">434</div>
                <div class="kanji">帆</div>
                <div class="keyword" style="display: none">sail</div>
            </div>

            <div class="divTableCell" id="435">
                <div class="framenr">435</div>
                <div class="kanji">幅</div>
                <div class="keyword" style="display: none">hanging scroll</div>
            </div>

            <div class="divTableCell" id="436">
                <div class="framenr">436</div>
                <div class="kanji">帽</div>
                <div class="keyword" style="display: none">cap</div>
            </div>

            <div class="divTableCell" id="437">
                <div class="framenr">437</div>
                <div class="kanji">幕</div>
                <div class="keyword" style="display: none">curtain</div>
            </div>

            <div class="divTableCell" id="438">
                <div class="framenr">438</div>
                <div class="kanji">幌</div>
                <div class="keyword" style="display: none">canopy</div>
            </div>

            <div class="divTableCell" id="439">
                <div class="framenr">439</div>
                <div class="kanji">錦</div>
                <div class="keyword" style="display: none">brocade</div>
            </div>

            <div class="divTableCell" id="440">
                <div class="framenr">440</div>
                <div class="kanji">市</div>
                <div class="keyword" style="display: none">market</div>
            </div>

            <div class="divTableCell" id="441">
                <div class="framenr">441</div>
                <div class="kanji">柿</div>
                <div class="keyword" style="display: none">persimmon</div>
            </div>

            <div class="divTableCell" id="442">
                <div class="framenr">442</div>
                <div class="kanji">姉</div>
                <div class="keyword" style="display: none">elder sister</div>
            </div>

            <div class="divTableCell" id="443">
                <div class="framenr">443</div>
                <div class="kanji">肺</div>
                <div class="keyword" style="display: none">lungs</div>
            </div>

            <div class="divTableCell" id="444">
                <div class="framenr">444</div>
                <div class="kanji">帯</div>
                <div class="keyword" style="display: none">sash</div>
            </div>

            <div class="divTableCell" id="445">
                <div class="framenr">445</div>
                <div class="kanji">滞</div>
                <div class="keyword" style="display: none">stagnate</div>
            </div>

            <div class="divTableCell" id="446">
                <div class="framenr">446</div>
                <div class="kanji">刺</div>
                <div class="keyword" style="display: none">thorn</div>
            </div>

            <div class="divTableCell" id="447">
                <div class="framenr">447</div>
                <div class="kanji">制</div>
                <div class="keyword" style="display: none">system</div>
            </div>

            <div class="divTableCell" id="448">
                <div class="framenr">448</div>
                <div class="kanji">製</div>
                <div class="keyword" style="display: none">made in...</div>
            </div>

            <div class="divTableCell" id="449">
                <div class="framenr">449</div>
                <div class="kanji">転</div>
                <div class="keyword" style="display: none">revolve</div>
            </div>

            <div class="divTableCell" id="450">
                <div class="framenr">450</div>
                <div class="kanji">芸</div>
                <div class="keyword" style="display: none">technique</div>
            </div>

            <div class="divTableCell" id="451">
                <div class="framenr">451</div>
                <div class="kanji">雨</div>
                <div class="keyword" style="display: none">rain</div>
            </div>

            <div class="divTableCell" id="452">
                <div class="framenr">452</div>
                <div class="kanji">雲</div>
                <div class="keyword" style="display: none">cloud</div>
            </div>

            <div class="divTableCell" id="453">
                <div class="framenr">453</div>
                <div class="kanji">曇</div>
                <div class="keyword" style="display: none">cloudy weather</div>
            </div>

            <div class="divTableCell" id="454">
                <div class="framenr">454</div>
                <div class="kanji">雷</div>
                <div class="keyword" style="display: none">thunder</div>
            </div>

            <div class="divTableCell" id="455">
                <div class="framenr">455</div>
                <div class="kanji">霜</div>
                <div class="keyword" style="display: none">frost</div>
            </div>

            <div class="divTableCell" id="456">
                <div class="framenr">456</div>
                <div class="kanji">冬</div>
                <div class="keyword" style="display: none">winter</div>
            </div>

            <div class="divTableCell" id="457">
                <div class="framenr">457</div>
                <div class="kanji">天</div>
                <div class="keyword" style="display: none">heavens</div>
            </div>

            <div class="divTableCell" id="458">
                <div class="framenr">458</div>
                <div class="kanji">妖</div>
                <div class="keyword" style="display: none">bewitched</div>
            </div>

            <div class="divTableCell" id="459">
                <div class="framenr">459</div>
                <div class="kanji">沃</div>
                <div class="keyword" style="display: none">irrigate</div>
            </div>

            <div class="divTableCell" id="460">
                <div class="framenr">460</div>
                <div class="kanji">橋</div>
                <div class="keyword" style="display: none">bridge</div>
            </div>

            <div class="divTableCell" id="461">
                <div class="framenr">461</div>
                <div class="kanji">嬌</div>
                <div class="keyword" style="display: none">attractive</div>
            </div>

            <div class="divTableCell" id="462">
                <div class="framenr">462</div>
                <div class="kanji">立</div>
                <div class="keyword" style="display: none">stand up</div>
            </div>

            <div class="divTableCell" id="463">
                <div class="framenr">463</div>
                <div class="kanji">泣</div>
                <div class="keyword" style="display: none">cry</div>
            </div>

            <div class="divTableCell" id="464">
                <div class="framenr">464</div>
                <div class="kanji">章</div>
                <div class="keyword" style="display: none">badge</div>
            </div>

            <div class="divTableCell" id="465">
                <div class="framenr">465</div>
                <div class="kanji">競</div>
                <div class="keyword" style="display: none">vie</div>
            </div>

            <div class="divTableCell" id="466">
                <div class="framenr">466</div>
                <div class="kanji">帝</div>
                <div class="keyword" style="display: none">sovereign</div>
            </div>

            <div class="divTableCell" id="467">
                <div class="framenr">467</div>
                <div class="kanji">諦</div>
                <div class="keyword" style="display: none">renunciation</div>
            </div>

            <div class="divTableCell" id="468">
                <div class="framenr">468</div>
                <div class="kanji">童</div>
                <div class="keyword" style="display: none">juvenile</div>
            </div>

            <div class="divTableCell" id="469">
                <div class="framenr">469</div>
                <div class="kanji">瞳</div>
                <div class="keyword" style="display: none">pupil</div>
            </div>

            <div class="divTableCell" id="470">
                <div class="framenr">470</div>
                <div class="kanji">鐘</div>
                <div class="keyword" style="display: none">bell</div>
            </div>

            <div class="divTableCell" id="471">
                <div class="framenr">471</div>
                <div class="kanji">商</div>
                <div class="keyword" style="display: none">make a deal</div>
            </div>

            <div class="divTableCell" id="472">
                <div class="framenr">472</div>
                <div class="kanji">嫡</div>
                <div class="keyword" style="display: none">legitimate wife</div>
            </div>

            <div class="divTableCell" id="473">
                <div class="framenr">473</div>
                <div class="kanji">適</div>
                <div class="keyword" style="display: none">suitable</div>
            </div>

            <div class="divTableCell" id="474">
                <div class="framenr">474</div>
                <div class="kanji">滴</div>
                <div class="keyword" style="display: none">drip</div>
            </div>

            <div class="divTableCell" id="475">
                <div class="framenr">475</div>
                <div class="kanji">敵</div>
                <div class="keyword" style="display: none">enemy</div>
            </div>

            <div class="divTableCell" id="476">
                <div class="framenr">476</div>
                <div class="kanji">匕</div>
                <div class="keyword" style="display: none">spoon</div>
            </div>

            <div class="divTableCell" id="477">
                <div class="framenr">477</div>
                <div class="kanji">叱</div>
                <div class="keyword" style="display: none">scold</div>
            </div>

            <div class="divTableCell" id="478">
                <div class="framenr">478</div>
                <div class="kanji">匂</div>
                <div class="keyword" style="display: none">aroma</div>
            </div>

            <div class="divTableCell" id="479">
                <div class="framenr">479</div>
                <div class="kanji">頃</div>
                <div class="keyword" style="display: none">about that time</div>
            </div>

            <div class="divTableCell" id="480">
                <div class="framenr">480</div>
                <div class="kanji">北</div>
                <div class="keyword" style="display: none">north</div>
            </div>

            <div class="divTableCell" id="481">
                <div class="framenr">481</div>
                <div class="kanji">背</div>
                <div class="keyword" style="display: none">stature</div>
            </div>

            <div class="divTableCell" id="482">
                <div class="framenr">482</div>
                <div class="kanji">比</div>
                <div class="keyword" style="display: none">compare</div>
            </div>

            <div class="divTableCell" id="483">
                <div class="framenr">483</div>
                <div class="kanji">昆</div>
                <div class="keyword" style="display: none">descendants</div>
            </div>

            <div class="divTableCell" id="484">
                <div class="framenr">484</div>
                <div class="kanji">皆</div>
                <div class="keyword" style="display: none">all</div>
            </div>

            <div class="divTableCell" id="485">
                <div class="framenr">485</div>
                <div class="kanji">楷</div>
                <div class="keyword" style="display: none">block letters</div>
            </div>

            <div class="divTableCell" id="486">
                <div class="framenr">486</div>
                <div class="kanji">諧</div>
                <div class="keyword" style="display: none">orderliness/harmony</div>
            </div>

            <div class="divTableCell" id="487">
                <div class="framenr">487</div>
                <div class="kanji">混</div>
                <div class="keyword" style="display: none">mix</div>
            </div>

            <div class="divTableCell" id="488">
                <div class="framenr">488</div>
                <div class="kanji">渇</div>
                <div class="keyword" style="display: none">thirst</div>
            </div>

            <div class="divTableCell" id="489">
                <div class="framenr">489</div>
                <div class="kanji">謁</div>
                <div class="keyword" style="display: none">audience</div>
            </div>

            <div class="divTableCell" id="490">
                <div class="framenr">490</div>
                <div class="kanji">褐</div>
                <div class="keyword" style="display: none">brown</div>
            </div>

            <div class="divTableCell" id="491">
                <div class="framenr">491</div>
                <div class="kanji">喝</div>
                <div class="keyword" style="display: none">hoarse</div>
            </div>

            <div class="divTableCell" id="492">
                <div class="framenr">492</div>
                <div class="kanji">葛</div>
                <div class="keyword" style="display: none">kudzu</div>
            </div>

            <div class="divTableCell" id="493">
                <div class="framenr">493</div>
                <div class="kanji">旨</div>
                <div class="keyword" style="display: none">delicious</div>
            </div>

            <div class="divTableCell" id="494">
                <div class="framenr">494</div>
                <div class="kanji">脂</div>
                <div class="keyword" style="display: none">fat</div>
            </div>

            <div class="divTableCell" id="495">
                <div class="framenr">495</div>
                <div class="kanji">詣</div>
                <div class="keyword" style="display: none">visit a shrine</div>
            </div>

            <div class="divTableCell" id="496">
                <div class="framenr">496</div>
                <div class="kanji">壱</div>
                <div class="keyword" style="display: none">I (one)</div>
            </div>

            <div class="divTableCell" id="497">
                <div class="framenr">497</div>
                <div class="kanji">毎</div>
                <div class="keyword" style="display: none">every</div>
            </div>

            <div class="divTableCell" id="498">
                <div class="framenr">498</div>
                <div class="kanji">敏</div>
                <div class="keyword" style="display: none">cleverness</div>
            </div>

            <div class="divTableCell" id="499">
                <div class="framenr">499</div>
                <div class="kanji">梅</div>
                <div class="keyword" style="display: none">plum</div>
            </div>

            <div class="divTableCell" id="500">
                <div class="framenr">500</div>
                <div class="kanji">海</div>
                <div class="keyword" style="display: none">sea</div>
            </div>

            <div class="divTableCell" id="501">
                <div class="framenr">501</div>
                <div class="kanji">乞</div>
                <div class="keyword" style="display: none">beg</div>
            </div>

            <div class="divTableCell" id="502">
                <div class="framenr">502</div>
                <div class="kanji">乾</div>
                <div class="keyword" style="display: none">drought</div>
            </div>

            <div class="divTableCell" id="503">
                <div class="framenr">503</div>
                <div class="kanji">腹</div>
                <div class="keyword" style="display: none">abdomen</div>
            </div>

            <div class="divTableCell" id="504">
                <div class="framenr">504</div>
                <div class="kanji">複</div>
                <div class="keyword" style="display: none">duplicate</div>
            </div>

            <div class="divTableCell" id="505">
                <div class="framenr">505</div>
                <div class="kanji">欠</div>
                <div class="keyword" style="display: none">lack</div>
            </div>

            <div class="divTableCell" id="506">
                <div class="framenr">506</div>
                <div class="kanji">吹</div>
                <div class="keyword" style="display: none">blow</div>
            </div>

            <div class="divTableCell" id="507">
                <div class="framenr">507</div>
                <div class="kanji">炊</div>
                <div class="keyword" style="display: none">cook</div>
            </div>

            <div class="divTableCell" id="508">
                <div class="framenr">508</div>
                <div class="kanji">歌</div>
                <div class="keyword" style="display: none">song</div>
            </div>

            <div class="divTableCell" id="509">
                <div class="framenr">509</div>
                <div class="kanji">軟</div>
                <div class="keyword" style="display: none">soft</div>
            </div>

            <div class="divTableCell" id="510">
                <div class="framenr">510</div>
                <div class="kanji">次</div>
                <div class="keyword" style="display: none">next</div>
            </div>

            <div class="divTableCell" id="511">
                <div class="framenr">511</div>
                <div class="kanji">茨</div>
                <div class="keyword" style="display: none">briar</div>
            </div>

            <div class="divTableCell" id="512">
                <div class="framenr">512</div>
                <div class="kanji">資</div>
                <div class="keyword" style="display: none">assets</div>
            </div>

            <div class="divTableCell" id="513">
                <div class="framenr">513</div>
                <div class="kanji">姿</div>
                <div class="keyword" style="display: none">figure</div>
            </div>

            <div class="divTableCell" id="514">
                <div class="framenr">514</div>
                <div class="kanji">諮</div>
                <div class="keyword" style="display: none">consult with</div>
            </div>

            <div class="divTableCell" id="515">
                <div class="framenr">515</div>
                <div class="kanji">賠</div>
                <div class="keyword" style="display: none">compensation</div>
            </div>

            <div class="divTableCell" id="516">
                <div class="framenr">516</div>
                <div class="kanji">培</div>
                <div class="keyword" style="display: none">cultivate</div>
            </div>

            <div class="divTableCell" id="517">
                <div class="framenr">517</div>
                <div class="kanji">剖</div>
                <div class="keyword" style="display: none">divide</div>
            </div>

            <div class="divTableCell" id="518">
                <div class="framenr">518</div>
                <div class="kanji">音</div>
                <div class="keyword" style="display: none">sound</div>
            </div>

            <div class="divTableCell" id="519">
                <div class="framenr">519</div>
                <div class="kanji">暗</div>
                <div class="keyword" style="display: none">darkness</div>
            </div>

            <div class="divTableCell" id="520">
                <div class="framenr">520</div>
                <div class="kanji">韻</div>
                <div class="keyword" style="display: none">rhyme</div>
            </div>

            <div class="divTableCell" id="521">
                <div class="framenr">521</div>
                <div class="kanji">識</div>
                <div class="keyword" style="display: none">discriminating</div>
            </div>

            <div class="divTableCell" id="522">
                <div class="framenr">522</div>
                <div class="kanji">鏡</div>
                <div class="keyword" style="display: none">mirror</div>
            </div>

            <div class="divTableCell" id="523">
                <div class="framenr">523</div>
                <div class="kanji">境</div>
                <div class="keyword" style="display: none">boundary</div>
            </div>

            <div class="divTableCell" id="524">
                <div class="framenr">524</div>
                <div class="kanji">亡</div>
                <div class="keyword" style="display: none">deceased</div>
            </div>

            <div class="divTableCell" id="525">
                <div class="framenr">525</div>
                <div class="kanji">盲</div>
                <div class="keyword" style="display: none">blind</div>
            </div>

            <div class="divTableCell" id="526">
                <div class="framenr">526</div>
                <div class="kanji">妄</div>
                <div class="keyword" style="display: none">delusion</div>
            </div>

            <div class="divTableCell" id="527">
                <div class="framenr">527</div>
                <div class="kanji">荒</div>
                <div class="keyword" style="display: none">laid waste</div>
            </div>

            <div class="divTableCell" id="528">
                <div class="framenr">528</div>
                <div class="kanji">望</div>
                <div class="keyword" style="display: none">ambition</div>
            </div>

            <div class="divTableCell" id="529">
                <div class="framenr">529</div>
                <div class="kanji">方</div>
                <div class="keyword" style="display: none">direction</div>
            </div>

            <div class="divTableCell" id="530">
                <div class="framenr">530</div>
                <div class="kanji">妨</div>
                <div class="keyword" style="display: none">disturb</div>
            </div>

            <div class="divTableCell" id="531">
                <div class="framenr">531</div>
                <div class="kanji">坊</div>
                <div class="keyword" style="display: none">boy</div>
            </div>

            <div class="divTableCell" id="532">
                <div class="framenr">532</div>
                <div class="kanji">芳</div>
                <div class="keyword" style="display: none">perfumed</div>
            </div>

            <div class="divTableCell" id="533">
                <div class="framenr">533</div>
                <div class="kanji">肪</div>
                <div class="keyword" style="display: none">obese</div>
            </div>

            <div class="divTableCell" id="534">
                <div class="framenr">534</div>
                <div class="kanji">訪</div>
                <div class="keyword" style="display: none">call on</div>
            </div>

            <div class="divTableCell" id="535">
                <div class="framenr">535</div>
                <div class="kanji">放</div>
                <div class="keyword" style="display: none">set free</div>
            </div>

            <div class="divTableCell" id="536">
                <div class="framenr">536</div>
                <div class="kanji">激</div>
                <div class="keyword" style="display: none">violent</div>
            </div>

            <div class="divTableCell" id="537">
                <div class="framenr">537</div>
                <div class="kanji">脱</div>
                <div class="keyword" style="display: none">undress</div>
            </div>

            <div class="divTableCell" id="538">
                <div class="framenr">538</div>
                <div class="kanji">説</div>
                <div class="keyword" style="display: none">explanation,rumor</div>
            </div>

            <div class="divTableCell" id="539">
                <div class="framenr">539</div>
                <div class="kanji">鋭</div>
                <div class="keyword" style="display: none">pointed</div>
            </div>

            <div class="divTableCell" id="540">
                <div class="framenr">540</div>
                <div class="kanji">曽</div>
                <div class="keyword" style="display: none">formerly</div>
            </div>

            <div class="divTableCell" id="541">
                <div class="framenr">541</div>
                <div class="kanji">増</div>
                <div class="keyword" style="display: none">increase</div>
            </div>

            <div class="divTableCell" id="542">
                <div class="framenr">542</div>
                <div class="kanji">贈</div>
                <div class="keyword" style="display: none">presents</div>
            </div>

            <div class="divTableCell" id="543">
                <div class="framenr">543</div>
                <div class="kanji">東</div>
                <div class="keyword" style="display: none">east</div>
            </div>

            <div class="divTableCell" id="544">
                <div class="framenr">544</div>
                <div class="kanji">棟</div>
                <div class="keyword" style="display: none">ridgepole</div>
            </div>

            <div class="divTableCell" id="545">
                <div class="framenr">545</div>
                <div class="kanji">凍</div>
                <div class="keyword" style="display: none">frozen</div>
            </div>

            <div class="divTableCell" id="546">
                <div class="framenr">546</div>
                <div class="kanji">妊</div>
                <div class="keyword" style="display: none">pregnancy</div>
            </div>

            <div class="divTableCell" id="547">
                <div class="framenr">547</div>
                <div class="kanji">廷</div>
                <div class="keyword" style="display: none">courts</div>
            </div>

            <div class="divTableCell" id="548">
                <div class="framenr">548</div>
                <div class="kanji">染</div>
                <div class="keyword" style="display: none">dye</div>
            </div>

            <div class="divTableCell" id="549">
                <div class="framenr">549</div>
                <div class="kanji">燃</div>
                <div class="keyword" style="display: none">burn</div>
            </div>

            <div class="divTableCell" id="550">
                <div class="framenr">550</div>
                <div class="kanji">賓</div>
                <div class="keyword" style="display: none">V.I.P.</div>
            </div>

            <div class="divTableCell" id="551">
                <div class="framenr">551</div>
                <div class="kanji">歳</div>
                <div class="keyword" style="display: none">year-end</div>
            </div>

            <div class="divTableCell" id="552">
                <div class="framenr">552</div>
                <div class="kanji">県</div>
                <div class="keyword" style="display: none">prefecture</div>
            </div>

            <div class="divTableCell" id="553">
                <div class="framenr">553</div>
                <div class="kanji">栃</div>
                <div class="keyword" style="display: none">horse chestnut</div>
            </div>

            <div class="divTableCell" id="554">
                <div class="framenr">554</div>
                <div class="kanji">地</div>
                <div class="keyword" style="display: none">ground</div>
            </div>

            <div class="divTableCell" id="555">
                <div class="framenr">555</div>
                <div class="kanji">池</div>
                <div class="keyword" style="display: none">pond</div>
            </div>

            <div class="divTableCell" id="556">
                <div class="framenr">556</div>
                <div class="kanji">虫</div>
                <div class="keyword" style="display: none">insect</div>
            </div>

            <div class="divTableCell" id="557">
                <div class="framenr">557</div>
                <div class="kanji">蛍</div>
                <div class="keyword" style="display: none">lightning bug</div>
            </div>

            <div class="divTableCell" id="558">
                <div class="framenr">558</div>
                <div class="kanji">蛇</div>
                <div class="keyword" style="display: none">snake</div>
            </div>

            <div class="divTableCell" id="559">
                <div class="framenr">559</div>
                <div class="kanji">虹</div>
                <div class="keyword" style="display: none">rainbow</div>
            </div>

            <div class="divTableCell" id="560">
                <div class="framenr">560</div>
                <div class="kanji">蝶</div>
                <div class="keyword" style="display: none">butterfly</div>
            </div>

            <div class="divTableCell" id="561">
                <div class="framenr">561</div>
                <div class="kanji">独</div>
                <div class="keyword" style="display: none">single</div>
            </div>

            <div class="divTableCell" id="562">
                <div class="framenr">562</div>
                <div class="kanji">蚕</div>
                <div class="keyword" style="display: none">silkworm</div>
            </div>

            <div class="divTableCell" id="563">
                <div class="framenr">563</div>
                <div class="kanji">風</div>
                <div class="keyword" style="display: none">wind</div>
            </div>

            <div class="divTableCell" id="564">
                <div class="framenr">564</div>
                <div class="kanji">己</div>
                <div class="keyword" style="display: none">self</div>
            </div>

            <div class="divTableCell" id="565">
                <div class="framenr">565</div>
                <div class="kanji">起</div>
                <div class="keyword" style="display: none">rouse</div>
            </div>

            <div class="divTableCell" id="566">
                <div class="framenr">566</div>
                <div class="kanji">妃</div>
                <div class="keyword" style="display: none">queen</div>
            </div>

            <div class="divTableCell" id="567">
                <div class="framenr">567</div>
                <div class="kanji">改</div>
                <div class="keyword" style="display: none">reformation</div>
            </div>

            <div class="divTableCell" id="568">
                <div class="framenr">568</div>
                <div class="kanji">記</div>
                <div class="keyword" style="display: none">scribe</div>
            </div>

            <div class="divTableCell" id="569">
                <div class="framenr">569</div>
                <div class="kanji">包</div>
                <div class="keyword" style="display: none">wrap</div>
            </div>

            <div class="divTableCell" id="570">
                <div class="framenr">570</div>
                <div class="kanji">胞</div>
                <div class="keyword" style="display: none">placenta</div>
            </div>

            <div class="divTableCell" id="571">
                <div class="framenr">571</div>
                <div class="kanji">砲</div>
                <div class="keyword" style="display: none">cannon</div>
            </div>

            <div class="divTableCell" id="572">
                <div class="framenr">572</div>
                <div class="kanji">泡</div>
                <div class="keyword" style="display: none">bubble</div>
            </div>

            <div class="divTableCell" id="573">
                <div class="framenr">573</div>
                <div class="kanji">亀</div>
                <div class="keyword" style="display: none">tortoise</div>
            </div>

            <div class="divTableCell" id="574">
                <div class="framenr">574</div>
                <div class="kanji">電</div>
                <div class="keyword" style="display: none">electricity</div>
            </div>

            <div class="divTableCell" id="575">
                <div class="framenr">575</div>
                <div class="kanji">竜</div>
                <div class="keyword" style="display: none">dragon</div>
            </div>

            <div class="divTableCell" id="576">
                <div class="framenr">576</div>
                <div class="kanji">滝</div>
                <div class="keyword" style="display: none">waterfall</div>
            </div>

            <div class="divTableCell" id="577">
                <div class="framenr">577</div>
                <div class="kanji">豚</div>
                <div class="keyword" style="display: none">pork</div>
            </div>

            <div class="divTableCell" id="578">
                <div class="framenr">578</div>
                <div class="kanji">逐</div>
                <div class="keyword" style="display: none">pursue</div>
            </div>

            <div class="divTableCell" id="579">
                <div class="framenr">579</div>
                <div class="kanji">遂</div>
                <div class="keyword" style="display: none">consummate</div>
            </div>

            <div class="divTableCell" id="580">
                <div class="framenr">580</div>
                <div class="kanji">家</div>
                <div class="keyword" style="display: none">house</div>
            </div>

            <div class="divTableCell" id="581">
                <div class="framenr">581</div>
                <div class="kanji">嫁</div>
                <div class="keyword" style="display: none">marry into</div>
            </div>

            <div class="divTableCell" id="582">
                <div class="framenr">582</div>
                <div class="kanji">豪</div>
                <div class="keyword" style="display: none">overpowering</div>
            </div>

            <div class="divTableCell" id="583">
                <div class="framenr">583</div>
                <div class="kanji">腸</div>
                <div class="keyword" style="display: none">intestines</div>
            </div>

            <div class="divTableCell" id="584">
                <div class="framenr">584</div>
                <div class="kanji">場</div>
                <div class="keyword" style="display: none">location</div>
            </div>

            <div class="divTableCell" id="585">
                <div class="framenr">585</div>
                <div class="kanji">湯</div>
                <div class="keyword" style="display: none">hot water</div>
            </div>

            <div class="divTableCell" id="586">
                <div class="framenr">586</div>
                <div class="kanji">羊</div>
                <div class="keyword" style="display: none">sheep</div>
            </div>

            <div class="divTableCell" id="587">
                <div class="framenr">587</div>
                <div class="kanji">美</div>
                <div class="keyword" style="display: none">beauty</div>
            </div>

            <div class="divTableCell" id="588">
                <div class="framenr">588</div>
                <div class="kanji">洋</div>
                <div class="keyword" style="display: none">ocean</div>
            </div>

            <div class="divTableCell" id="589">
                <div class="framenr">589</div>
                <div class="kanji">詳</div>
                <div class="keyword" style="display: none">detailed</div>
            </div>

            <div class="divTableCell" id="590">
                <div class="framenr">590</div>
                <div class="kanji">鮮</div>
                <div class="keyword" style="display: none">fresh</div>
            </div>

            <div class="divTableCell" id="591">
                <div class="framenr">591</div>
                <div class="kanji">達</div>
                <div class="keyword" style="display: none">accomplished</div>
            </div>

            <div class="divTableCell" id="592">
                <div class="framenr">592</div>
                <div class="kanji">羨</div>
                <div class="keyword" style="display: none">envious</div>
            </div>

            <div class="divTableCell" id="593">
                <div class="framenr">593</div>
                <div class="kanji">差</div>
                <div class="keyword" style="display: none">distinction</div>
            </div>

            <div class="divTableCell" id="594">
                <div class="framenr">594</div>
                <div class="kanji">着</div>
                <div class="keyword" style="display: none">don</div>
            </div>

            <div class="divTableCell" id="595">
                <div class="framenr">595</div>
                <div class="kanji">唯</div>
                <div class="keyword" style="display: none">solely</div>
            </div>

            <div class="divTableCell" id="596">
                <div class="framenr">596</div>
                <div class="kanji">堆</div>
                <div class="keyword" style="display: none">piled high</div>
            </div>

            <div class="divTableCell" id="597">
                <div class="framenr">597</div>
                <div class="kanji">椎</div>
                <div class="keyword" style="display: none">sweet oak</div>
            </div>

            <div class="divTableCell" id="598">
                <div class="framenr">598</div>
                <div class="kanji">誰</div>
                <div class="keyword" style="display: none">who?</div>
            </div>

            <div class="divTableCell" id="599">
                <div class="framenr">599</div>
                <div class="kanji">焦</div>
                <div class="keyword" style="display: none">char</div>
            </div>

            <div class="divTableCell" id="600">
                <div class="framenr">600</div>
                <div class="kanji">礁</div>
                <div class="keyword" style="display: none">reef</div>
            </div>

            <div class="divTableCell" id="601">
                <div class="framenr">601</div>
                <div class="kanji">集</div>
                <div class="keyword" style="display: none">gather</div>
            </div>

            <div class="divTableCell" id="602">
                <div class="framenr">602</div>
                <div class="kanji">准</div>
                <div class="keyword" style="display: none">quasi-</div>
            </div>

            <div class="divTableCell" id="603">
                <div class="framenr">603</div>
                <div class="kanji">進</div>
                <div class="keyword" style="display: none">advance</div>
            </div>

            <div class="divTableCell" id="604">
                <div class="framenr">604</div>
                <div class="kanji">雑</div>
                <div class="keyword" style="display: none">miscellaneous</div>
            </div>

            <div class="divTableCell" id="605">
                <div class="framenr">605</div>
                <div class="kanji">雌</div>
                <div class="keyword" style="display: none">female</div>
            </div>

            <div class="divTableCell" id="606">
                <div class="framenr">606</div>
                <div class="kanji">準</div>
                <div class="keyword" style="display: none">semi-</div>
            </div>

            <div class="divTableCell" id="607">
                <div class="framenr">607</div>
                <div class="kanji">奮</div>
                <div class="keyword" style="display: none">stirred up</div>
            </div>

            <div class="divTableCell" id="608">
                <div class="framenr">608</div>
                <div class="kanji">奪</div>
                <div class="keyword" style="display: none">rob</div>
            </div>

            <div class="divTableCell" id="609">
                <div class="framenr">609</div>
                <div class="kanji">確</div>
                <div class="keyword" style="display: none">assurance</div>
            </div>

            <div class="divTableCell" id="610">
                <div class="framenr">610</div>
                <div class="kanji">午</div>
                <div class="keyword" style="display: none">noon</div>
            </div>

            <div class="divTableCell" id="611">
                <div class="framenr">611</div>
                <div class="kanji">許</div>
                <div class="keyword" style="display: none">permit</div>
            </div>

            <div class="divTableCell" id="612">
                <div class="framenr">612</div>
                <div class="kanji">歓</div>
                <div class="keyword" style="display: none">delight</div>
            </div>

            <div class="divTableCell" id="613">
                <div class="framenr">613</div>
                <div class="kanji">権</div>
                <div class="keyword" style="display: none">authority</div>
            </div>

            <div class="divTableCell" id="614">
                <div class="framenr">614</div>
                <div class="kanji">観</div>
                <div class="keyword" style="display: none">outlook</div>
            </div>

            <div class="divTableCell" id="615">
                <div class="framenr">615</div>
                <div class="kanji">羽</div>
                <div class="keyword" style="display: none">feathers</div>
            </div>

            <div class="divTableCell" id="616">
                <div class="framenr">616</div>
                <div class="kanji">習</div>
                <div class="keyword" style="display: none">learn</div>
            </div>

            <div class="divTableCell" id="617">
                <div class="framenr">617</div>
                <div class="kanji">翌</div>
                <div class="keyword" style="display: none">the following</div>
            </div>

            <div class="divTableCell" id="618">
                <div class="framenr">618</div>
                <div class="kanji">曜</div>
                <div class="keyword" style="display: none">weekday</div>
            </div>

            <div class="divTableCell" id="619">
                <div class="framenr">619</div>
                <div class="kanji">濯</div>
                <div class="keyword" style="display: none">laundry</div>
            </div>

            <div class="divTableCell" id="620">
                <div class="framenr">620</div>
                <div class="kanji">曰</div>
                <div class="keyword" style="display: none">sayeth</div>
            </div>

            <div class="divTableCell" id="621">
                <div class="framenr">621</div>
                <div class="kanji">困</div>
                <div class="keyword" style="display: none">quandary</div>
            </div>

            <div class="divTableCell" id="622">
                <div class="framenr">622</div>
                <div class="kanji">固</div>
                <div class="keyword" style="display: none">harden</div>
            </div>

            <div class="divTableCell" id="623">
                <div class="framenr">623</div>
                <div class="kanji">錮</div>
                <div class="keyword" style="display: none">weld</div>
            </div>

            <div class="divTableCell" id="624">
                <div class="framenr">624</div>
                <div class="kanji">国</div>
                <div class="keyword" style="display: none">country</div>
            </div>

            <div class="divTableCell" id="625">
                <div class="framenr">625</div>
                <div class="kanji">団</div>
                <div class="keyword" style="display: none">group</div>
            </div>

            <div class="divTableCell" id="626">
                <div class="framenr">626</div>
                <div class="kanji">因</div>
                <div class="keyword" style="display: none">cause</div>
            </div>

            <div class="divTableCell" id="627">
                <div class="framenr">627</div>
                <div class="kanji">姻</div>
                <div class="keyword" style="display: none">matrimony</div>
            </div>

            <div class="divTableCell" id="628">
                <div class="framenr">628</div>
                <div class="kanji">咽</div>
                <div class="keyword" style="display: none">windpipe</div>
            </div>

            <div class="divTableCell" id="629">
                <div class="framenr">629</div>
                <div class="kanji">園</div>
                <div class="keyword" style="display: none">park</div>
            </div>

            <div class="divTableCell" id="630">
                <div class="framenr">630</div>
                <div class="kanji">回</div>
                <div class="keyword" style="display: none">-times</div>
            </div>

            <div class="divTableCell" id="631">
                <div class="framenr">631</div>
                <div class="kanji">壇</div>
                <div class="keyword" style="display: none">podium</div>
            </div>

            <div class="divTableCell" id="632">
                <div class="framenr">632</div>
                <div class="kanji">店</div>
                <div class="keyword" style="display: none">store</div>
            </div>

            <div class="divTableCell" id="633">
                <div class="framenr">633</div>
                <div class="kanji">庫</div>
                <div class="keyword" style="display: none">warehouse</div>
            </div>

            <div class="divTableCell" id="634">
                <div class="framenr">634</div>
                <div class="kanji">庭</div>
                <div class="keyword" style="display: none">courtyard</div>
            </div>

            <div class="divTableCell" id="635">
                <div class="framenr">635</div>
                <div class="kanji">庁</div>
                <div class="keyword" style="display: none">government office</div>
            </div>

            <div class="divTableCell" id="636">
                <div class="framenr">636</div>
                <div class="kanji">床</div>
                <div class="keyword" style="display: none">bed</div>
            </div>

            <div class="divTableCell" id="637">
                <div class="framenr">637</div>
                <div class="kanji">麻</div>
                <div class="keyword" style="display: none">hemp</div>
            </div>

            <div class="divTableCell" id="638">
                <div class="framenr">638</div>
                <div class="kanji">磨</div>
                <div class="keyword" style="display: none">grind</div>
            </div>

            <div class="divTableCell" id="639">
                <div class="framenr">639</div>
                <div class="kanji">心</div>
                <div class="keyword" style="display: none">heart</div>
            </div>

            <div class="divTableCell" id="640">
                <div class="framenr">640</div>
                <div class="kanji">忘</div>
                <div class="keyword" style="display: none">forget</div>
            </div>

            <div class="divTableCell" id="641">
                <div class="framenr">641</div>
                <div class="kanji">恣</div>
                <div class="keyword" style="display: none">selfish</div>
            </div>

            <div class="divTableCell" id="642">
                <div class="framenr">642</div>
                <div class="kanji">忍</div>
                <div class="keyword" style="display: none">endure</div>
            </div>

            <div class="divTableCell" id="643">
                <div class="framenr">643</div>
                <div class="kanji">認</div>
                <div class="keyword" style="display: none">acknowledge</div>
            </div>

            <div class="divTableCell" id="644">
                <div class="framenr">644</div>
                <div class="kanji">忌</div>
                <div class="keyword" style="display: none">mourning</div>
            </div>

            <div class="divTableCell" id="645">
                <div class="framenr">645</div>
                <div class="kanji">志</div>
                <div class="keyword" style="display: none">intention</div>
            </div>

            <div class="divTableCell" id="646">
                <div class="framenr">646</div>
                <div class="kanji">誌</div>
                <div class="keyword" style="display: none">document</div>
            </div>

            <div class="divTableCell" id="647">
                <div class="framenr">647</div>
                <div class="kanji">芯</div>
                <div class="keyword" style="display: none">wick</div>
            </div>

            <div class="divTableCell" id="648">
                <div class="framenr">648</div>
                <div class="kanji">忠</div>
                <div class="keyword" style="display: none">loyalty</div>
            </div>

            <div class="divTableCell" id="649">
                <div class="framenr">649</div>
                <div class="kanji">串</div>
                <div class="keyword" style="display: none">shish kebab</div>
            </div>

            <div class="divTableCell" id="650">
                <div class="framenr">650</div>
                <div class="kanji">患</div>
                <div class="keyword" style="display: none">afflicted</div>
            </div>

            <div class="divTableCell" id="651">
                <div class="framenr">651</div>
                <div class="kanji">思</div>
                <div class="keyword" style="display: none">think</div>
            </div>

            <div class="divTableCell" id="652">
                <div class="framenr">652</div>
                <div class="kanji">恩</div>
                <div class="keyword" style="display: none">grace</div>
            </div>

            <div class="divTableCell" id="653">
                <div class="framenr">653</div>
                <div class="kanji">応</div>
                <div class="keyword" style="display: none">apply</div>
            </div>

            <div class="divTableCell" id="654">
                <div class="framenr">654</div>
                <div class="kanji">意</div>
                <div class="keyword" style="display: none">idea</div>
            </div>

            <div class="divTableCell" id="655">
                <div class="framenr">655</div>
                <div class="kanji">臆</div>
                <div class="keyword" style="display: none">cowardice</div>
            </div>

            <div class="divTableCell" id="656">
                <div class="framenr">656</div>
                <div class="kanji">想</div>
                <div class="keyword" style="display: none">concept</div>
            </div>

            <div class="divTableCell" id="657">
                <div class="framenr">657</div>
                <div class="kanji">息</div>
                <div class="keyword" style="display: none">breath</div>
            </div>

            <div class="divTableCell" id="658">
                <div class="framenr">658</div>
                <div class="kanji">憩</div>
                <div class="keyword" style="display: none">recess</div>
            </div>

            <div class="divTableCell" id="659">
                <div class="framenr">659</div>
                <div class="kanji">恵</div>
                <div class="keyword" style="display: none">favor</div>
            </div>

            <div class="divTableCell" id="660">
                <div class="framenr">660</div>
                <div class="kanji">恐</div>
                <div class="keyword" style="display: none">fear</div>
            </div>

            <div class="divTableCell" id="661">
                <div class="framenr">661</div>
                <div class="kanji">惑</div>
                <div class="keyword" style="display: none">beguile</div>
            </div>

            <div class="divTableCell" id="662">
                <div class="framenr">662</div>
                <div class="kanji">感</div>
                <div class="keyword" style="display: none">emotion</div>
            </div>

            <div class="divTableCell" id="663">
                <div class="framenr">663</div>
                <div class="kanji">憂</div>
                <div class="keyword" style="display: none">melancholy</div>
            </div>

            <div class="divTableCell" id="664">
                <div class="framenr">664</div>
                <div class="kanji">寡</div>
                <div class="keyword" style="display: none">widow</div>
            </div>

            <div class="divTableCell" id="665">
                <div class="framenr">665</div>
                <div class="kanji">忙</div>
                <div class="keyword" style="display: none">busy</div>
            </div>

            <div class="divTableCell" id="666">
                <div class="framenr">666</div>
                <div class="kanji">悦</div>
                <div class="keyword" style="display: none">ecstasy</div>
            </div>

            <div class="divTableCell" id="667">
                <div class="framenr">667</div>
                <div class="kanji">恒</div>
                <div class="keyword" style="display: none">constancy</div>
            </div>

            <div class="divTableCell" id="668">
                <div class="framenr">668</div>
                <div class="kanji">悼</div>
                <div class="keyword" style="display: none">lament</div>
            </div>

            <div class="divTableCell" id="669">
                <div class="framenr">669</div>
                <div class="kanji">悟</div>
                <div class="keyword" style="display: none">enlightenment</div>
            </div>

            <div class="divTableCell" id="670">
                <div class="framenr">670</div>
                <div class="kanji">怖</div>
                <div class="keyword" style="display: none">dreadful</div>
            </div>

            <div class="divTableCell" id="671">
                <div class="framenr">671</div>
                <div class="kanji">慌</div>
                <div class="keyword" style="display: none">disconcerted</div>
            </div>

            <div class="divTableCell" id="672">
                <div class="framenr">672</div>
                <div class="kanji">悔</div>
                <div class="keyword" style="display: none">repent</div>
            </div>

            <div class="divTableCell" id="673">
                <div class="framenr">673</div>
                <div class="kanji">憎</div>
                <div class="keyword" style="display: none">hate</div>
            </div>

            <div class="divTableCell" id="674">
                <div class="framenr">674</div>
                <div class="kanji">慣</div>
                <div class="keyword" style="display: none">accustomed</div>
            </div>

            <div class="divTableCell" id="675">
                <div class="framenr">675</div>
                <div class="kanji">愉</div>
                <div class="keyword" style="display: none">pleasure</div>
            </div>

            <div class="divTableCell" id="676">
                <div class="framenr">676</div>
                <div class="kanji">惰</div>
                <div class="keyword" style="display: none">lazy</div>
            </div>

            <div class="divTableCell" id="677">
                <div class="framenr">677</div>
                <div class="kanji">慎</div>
                <div class="keyword" style="display: none">humility</div>
            </div>

            <div class="divTableCell" id="678">
                <div class="framenr">678</div>
                <div class="kanji">憾</div>
                <div class="keyword" style="display: none">remorse</div>
            </div>

            <div class="divTableCell" id="679">
                <div class="framenr">679</div>
                <div class="kanji">憶</div>
                <div class="keyword" style="display: none">recollection</div>
            </div>

            <div class="divTableCell" id="680">
                <div class="framenr">680</div>
                <div class="kanji">惧</div>
                <div class="keyword" style="display: none">disquieting</div>
            </div>

            <div class="divTableCell" id="681">
                <div class="framenr">681</div>
                <div class="kanji">憧</div>
                <div class="keyword" style="display: none">yearn</div>
            </div>

            <div class="divTableCell" id="682">
                <div class="framenr">682</div>
                <div class="kanji">憬</div>
                <div class="keyword" style="display: none">hanker</div>
            </div>

            <div class="divTableCell" id="683">
                <div class="framenr">683</div>
                <div class="kanji">慕</div>
                <div class="keyword" style="display: none">pining</div>
            </div>

            <div class="divTableCell" id="684">
                <div class="framenr">684</div>
                <div class="kanji">添</div>
                <div class="keyword" style="display: none">annexed</div>
            </div>

            <div class="divTableCell" id="685">
                <div class="framenr">685</div>
                <div class="kanji">必</div>
                <div class="keyword" style="display: none">invariably</div>
            </div>

            <div class="divTableCell" id="686">
                <div class="framenr">686</div>
                <div class="kanji">泌</div>
                <div class="keyword" style="display: none">ooze</div>
            </div>

            <div class="divTableCell" id="687">
                <div class="framenr">687</div>
                <div class="kanji">手</div>
                <div class="keyword" style="display: none">hand</div>
            </div>

            <div class="divTableCell" id="688">
                <div class="framenr">688</div>
                <div class="kanji">看</div>
                <div class="keyword" style="display: none">watch over</div>
            </div>

            <div class="divTableCell" id="689">
                <div class="framenr">689</div>
                <div class="kanji">摩</div>
                <div class="keyword" style="display: none">chafe</div>
            </div>

            <div class="divTableCell" id="690">
                <div class="framenr">690</div>
                <div class="kanji">我</div>
                <div class="keyword" style="display: none">ego</div>
            </div>

            <div class="divTableCell" id="691">
                <div class="framenr">691</div>
                <div class="kanji">義</div>
                <div class="keyword" style="display: none">righteousness</div>
            </div>

            <div class="divTableCell" id="692">
                <div class="framenr">692</div>
                <div class="kanji">議</div>
                <div class="keyword" style="display: none">deliberation</div>
            </div>

            <div class="divTableCell" id="693">
                <div class="framenr">693</div>
                <div class="kanji">犠</div>
                <div class="keyword" style="display: none">sacrifice</div>
            </div>

            <div class="divTableCell" id="694">
                <div class="framenr">694</div>
                <div class="kanji">抹</div>
                <div class="keyword" style="display: none">rub</div>
            </div>

            <div class="divTableCell" id="695">
                <div class="framenr">695</div>
                <div class="kanji">拭</div>
                <div class="keyword" style="display: none">wipe</div>
            </div>

            <div class="divTableCell" id="696">
                <div class="framenr">696</div>
                <div class="kanji">拉</div>
                <div class="keyword" style="display: none">yank</div>
            </div>

            <div class="divTableCell" id="697">
                <div class="framenr">697</div>
                <div class="kanji">抱</div>
                <div class="keyword" style="display: none">embrace</div>
            </div>

            <div class="divTableCell" id="698">
                <div class="framenr">698</div>
                <div class="kanji">搭</div>
                <div class="keyword" style="display: none">board</div>
            </div>

            <div class="divTableCell" id="699">
                <div class="framenr">699</div>
                <div class="kanji">抄</div>
                <div class="keyword" style="display: none">extract</div>
            </div>

            <div class="divTableCell" id="700">
                <div class="framenr">700</div>
                <div class="kanji">抗</div>
                <div class="keyword" style="display: none">confront</div>
            </div>

            <div class="divTableCell" id="701">
                <div class="framenr">701</div>
                <div class="kanji">批</div>
                <div class="keyword" style="display: none">criticism</div>
            </div>

            <div class="divTableCell" id="702">
                <div class="framenr">702</div>
                <div class="kanji">招</div>
                <div class="keyword" style="display: none">beckon</div>
            </div>

            <div class="divTableCell" id="703">
                <div class="framenr">703</div>
                <div class="kanji">拓</div>
                <div class="keyword" style="display: none">clear the land</div>
            </div>

            <div class="divTableCell" id="704">
                <div class="framenr">704</div>
                <div class="kanji">拍</div>
                <div class="keyword" style="display: none">clap</div>
            </div>

            <div class="divTableCell" id="705">
                <div class="framenr">705</div>
                <div class="kanji">打</div>
                <div class="keyword" style="display: none">strike</div>
            </div>

            <div class="divTableCell" id="706">
                <div class="framenr">706</div>
                <div class="kanji">拘</div>
                <div class="keyword" style="display: none">arrest</div>
            </div>

            <div class="divTableCell" id="707">
                <div class="framenr">707</div>
                <div class="kanji">捨</div>
                <div class="keyword" style="display: none">discard</div>
            </div>

            <div class="divTableCell" id="708">
                <div class="framenr">708</div>
                <div class="kanji">拐</div>
                <div class="keyword" style="display: none">kidnap</div>
            </div>

            <div class="divTableCell" id="709">
                <div class="framenr">709</div>
                <div class="kanji">摘</div>
                <div class="keyword" style="display: none">pinch</div>
            </div>

            <div class="divTableCell" id="710">
                <div class="framenr">710</div>
                <div class="kanji">挑</div>
                <div class="keyword" style="display: none">challenge</div>
            </div>

            <div class="divTableCell" id="711">
                <div class="framenr">711</div>
                <div class="kanji">指</div>
                <div class="keyword" style="display: none">finger</div>
            </div>

            <div class="divTableCell" id="712">
                <div class="framenr">712</div>
                <div class="kanji">持</div>
                <div class="keyword" style="display: none">hold</div>
            </div>

            <div class="divTableCell" id="713">
                <div class="framenr">713</div>
                <div class="kanji">拶</div>
                <div class="keyword" style="display: none">imminent</div>
            </div>

            <div class="divTableCell" id="714">
                <div class="framenr">714</div>
                <div class="kanji">括</div>
                <div class="keyword" style="display: none">fasten</div>
            </div>

            <div class="divTableCell" id="715">
                <div class="framenr">715</div>
                <div class="kanji">揮</div>
                <div class="keyword" style="display: none">brandish</div>
            </div>

            <div class="divTableCell" id="716">
                <div class="framenr">716</div>
                <div class="kanji">推</div>
                <div class="keyword" style="display: none">conjecture</div>
            </div>

            <div class="divTableCell" id="717">
                <div class="framenr">717</div>
                <div class="kanji">揚</div>
                <div class="keyword" style="display: none">hoist</div>
            </div>

            <div class="divTableCell" id="718">
                <div class="framenr">718</div>
                <div class="kanji">提</div>
                <div class="keyword" style="display: none">propose</div>
            </div>

            <div class="divTableCell" id="719">
                <div class="framenr">719</div>
                <div class="kanji">損</div>
                <div class="keyword" style="display: none">damage</div>
            </div>

            <div class="divTableCell" id="720">
                <div class="framenr">720</div>
                <div class="kanji">拾</div>
                <div class="keyword" style="display: none">pick up</div>
            </div>

            <div class="divTableCell" id="721">
                <div class="framenr">721</div>
                <div class="kanji">担</div>
                <div class="keyword" style="display: none">shouldering</div>
            </div>

            <div class="divTableCell" id="722">
                <div class="framenr">722</div>
                <div class="kanji">拠</div>
                <div class="keyword" style="display: none">foothold</div>
            </div>

            <div class="divTableCell" id="723">
                <div class="framenr">723</div>
                <div class="kanji">描</div>
                <div class="keyword" style="display: none">sketch</div>
            </div>

            <div class="divTableCell" id="724">
                <div class="framenr">724</div>
                <div class="kanji">操</div>
                <div class="keyword" style="display: none">maneuver</div>
            </div>

            <div class="divTableCell" id="725">
                <div class="framenr">725</div>
                <div class="kanji">接</div>
                <div class="keyword" style="display: none">touch</div>
            </div>

            <div class="divTableCell" id="726">
                <div class="framenr">726</div>
                <div class="kanji">掲</div>
                <div class="keyword" style="display: none">put up a notice</div>
            </div>

            <div class="divTableCell" id="727">
                <div class="framenr">727</div>
                <div class="kanji">掛</div>
                <div class="keyword" style="display: none">hang</div>
            </div>

            <div class="divTableCell" id="728">
                <div class="framenr">728</div>
                <div class="kanji">捗</div>
                <div class="keyword" style="display: none">make headway</div>
            </div>

            <div class="divTableCell" id="729">
                <div class="framenr">729</div>
                <div class="kanji">研</div>
                <div class="keyword" style="display: none">polish</div>
            </div>

            <div class="divTableCell" id="730">
                <div class="framenr">730</div>
                <div class="kanji">戒</div>
                <div class="keyword" style="display: none">commandment</div>
            </div>

            <div class="divTableCell" id="731">
                <div class="framenr">731</div>
                <div class="kanji">弄</div>
                <div class="keyword" style="display: none">tinker with</div>
            </div>

            <div class="divTableCell" id="732">
                <div class="framenr">732</div>
                <div class="kanji">械</div>
                <div class="keyword" style="display: none">contraption</div>
            </div>

            <div class="divTableCell" id="733">
                <div class="framenr">733</div>
                <div class="kanji">鼻</div>
                <div class="keyword" style="display: none">nose</div>
            </div>

            <div class="divTableCell" id="734">
                <div class="framenr">734</div>
                <div class="kanji">刑</div>
                <div class="keyword" style="display: none">punish</div>
            </div>

            <div class="divTableCell" id="735">
                <div class="framenr">735</div>
                <div class="kanji">型</div>
                <div class="keyword" style="display: none">mould</div>
            </div>

            <div class="divTableCell" id="736">
                <div class="framenr">736</div>
                <div class="kanji">才</div>
                <div class="keyword" style="display: none">genius</div>
            </div>

            <div class="divTableCell" id="737">
                <div class="framenr">737</div>
                <div class="kanji">財</div>
                <div class="keyword" style="display: none">property</div>
            </div>

            <div class="divTableCell" id="738">
                <div class="framenr">738</div>
                <div class="kanji">材</div>
                <div class="keyword" style="display: none">lumber</div>
            </div>

            <div class="divTableCell" id="739">
                <div class="framenr">739</div>
                <div class="kanji">存</div>
                <div class="keyword" style="display: none">suppose</div>
            </div>

            <div class="divTableCell" id="740">
                <div class="framenr">740</div>
                <div class="kanji">在</div>
                <div class="keyword" style="display: none">exist</div>
            </div>

            <div class="divTableCell" id="741">
                <div class="framenr">741</div>
                <div class="kanji">乃</div>
                <div class="keyword" style="display: none">from</div>
            </div>

            <div class="divTableCell" id="742">
                <div class="framenr">742</div>
                <div class="kanji">携</div>
                <div class="keyword" style="display: none">portable</div>
            </div>

            <div class="divTableCell" id="743">
                <div class="framenr">743</div>
                <div class="kanji">及</div>
                <div class="keyword" style="display: none">reach out</div>
            </div>

            <div class="divTableCell" id="744">
                <div class="framenr">744</div>
                <div class="kanji">吸</div>
                <div class="keyword" style="display: none">suck</div>
            </div>

            <div class="divTableCell" id="745">
                <div class="framenr">745</div>
                <div class="kanji">扱</div>
                <div class="keyword" style="display: none">handle</div>
            </div>

            <div class="divTableCell" id="746">
                <div class="framenr">746</div>
                <div class="kanji">丈</div>
                <div class="keyword" style="display: none">length</div>
            </div>

            <div class="divTableCell" id="747">
                <div class="framenr">747</div>
                <div class="kanji">史</div>
                <div class="keyword" style="display: none">history</div>
            </div>

            <div class="divTableCell" id="748">
                <div class="framenr">748</div>
                <div class="kanji">吏</div>
                <div class="keyword" style="display: none">officer</div>
            </div>

            <div class="divTableCell" id="749">
                <div class="framenr">749</div>
                <div class="kanji">更</div>
                <div class="keyword" style="display: none">grow late</div>
            </div>

            <div class="divTableCell" id="750">
                <div class="framenr">750</div>
                <div class="kanji">硬</div>
                <div class="keyword" style="display: none">stiff</div>
            </div>

            <div class="divTableCell" id="751">
                <div class="framenr">751</div>
                <div class="kanji">梗</div>
                <div class="keyword" style="display: none">spiny(for the most part)</div>
            </div>

            <div class="divTableCell" id="752">
                <div class="framenr">752</div>
                <div class="kanji">又</div>
                <div class="keyword" style="display: none">or again</div>
            </div>

            <div class="divTableCell" id="753">
                <div class="framenr">753</div>
                <div class="kanji">双</div>
                <div class="keyword" style="display: none">pair</div>
            </div>

            <div class="divTableCell" id="754">
                <div class="framenr">754</div>
                <div class="kanji">桑</div>
                <div class="keyword" style="display: none">mulberry</div>
            </div>

            <div class="divTableCell" id="755">
                <div class="framenr">755</div>
                <div class="kanji">隻</div>
                <div class="keyword" style="display: none">vessels</div>
            </div>

            <div class="divTableCell" id="756">
                <div class="framenr">756</div>
                <div class="kanji">護</div>
                <div class="keyword" style="display: none">safeguard</div>
            </div>

            <div class="divTableCell" id="757">
                <div class="framenr">757</div>
                <div class="kanji">獲</div>
                <div class="keyword" style="display: none">seize</div>
            </div>

            <div class="divTableCell" id="758">
                <div class="framenr">758</div>
                <div class="kanji">奴</div>
                <div class="keyword" style="display: none">guy</div>
            </div>

            <div class="divTableCell" id="759">
                <div class="framenr">759</div>
                <div class="kanji">怒</div>
                <div class="keyword" style="display: none">angry</div>
            </div>

            <div class="divTableCell" id="760">
                <div class="framenr">760</div>
                <div class="kanji">友</div>
                <div class="keyword" style="display: none">friend</div>
            </div>

            <div class="divTableCell" id="761">
                <div class="framenr">761</div>
                <div class="kanji">抜</div>
                <div class="keyword" style="display: none">slip out</div>
            </div>

            <div class="divTableCell" id="762">
                <div class="framenr">762</div>
                <div class="kanji">投</div>
                <div class="keyword" style="display: none">throw</div>
            </div>

            <div class="divTableCell" id="763">
                <div class="framenr">763</div>
                <div class="kanji">没</div>
                <div class="keyword" style="display: none">drown</div>
            </div>

            <div class="divTableCell" id="764">
                <div class="framenr">764</div>
                <div class="kanji">股</div>
                <div class="keyword" style="display: none">thigh</div>
            </div>

            <div class="divTableCell" id="765">
                <div class="framenr">765</div>
                <div class="kanji">設</div>
                <div class="keyword" style="display: none">establishment</div>
            </div>

            <div class="divTableCell" id="766">
                <div class="framenr">766</div>
                <div class="kanji">撃</div>
                <div class="keyword" style="display: none">beat</div>
            </div>

            <div class="divTableCell" id="767">
                <div class="framenr">767</div>
                <div class="kanji">殻</div>
                <div class="keyword" style="display: none">husk</div>
            </div>

            <div class="divTableCell" id="768">
                <div class="framenr">768</div>
                <div class="kanji">支</div>
                <div class="keyword" style="display: none">branch</div>
            </div>

            <div class="divTableCell" id="769">
                <div class="framenr">769</div>
                <div class="kanji">技</div>
                <div class="keyword" style="display: none">skill</div>
            </div>

            <div class="divTableCell" id="770">
                <div class="framenr">770</div>
                <div class="kanji">枝</div>
                <div class="keyword" style="display: none">bough</div>
            </div>

            <div class="divTableCell" id="771">
                <div class="framenr">771</div>
                <div class="kanji">肢</div>
                <div class="keyword" style="display: none">limb</div>
            </div>

            <div class="divTableCell" id="772">
                <div class="framenr">772</div>
                <div class="kanji">茎</div>
                <div class="keyword" style="display: none">stalk</div>
            </div>

            <div class="divTableCell" id="773">
                <div class="framenr">773</div>
                <div class="kanji">怪</div>
                <div class="keyword" style="display: none">suspicious</div>
            </div>

            <div class="divTableCell" id="774">
                <div class="framenr">774</div>
                <div class="kanji">軽</div>
                <div class="keyword" style="display: none">lightly</div>
            </div>

            <div class="divTableCell" id="775">
                <div class="framenr">775</div>
                <div class="kanji">叔</div>
                <div class="keyword" style="display: none">uncle</div>
            </div>

            <div class="divTableCell" id="776">
                <div class="framenr">776</div>
                <div class="kanji">督</div>
                <div class="keyword" style="display: none">coach</div>
            </div>

            <div class="divTableCell" id="777">
                <div class="framenr">777</div>
                <div class="kanji">寂</div>
                <div class="keyword" style="display: none">loneliness</div>
            </div>

            <div class="divTableCell" id="778">
                <div class="framenr">778</div>
                <div class="kanji">淑</div>
                <div class="keyword" style="display: none">graceful</div>
            </div>

            <div class="divTableCell" id="779">
                <div class="framenr">779</div>
                <div class="kanji">反</div>
                <div class="keyword" style="display: none">anti-</div>
            </div>

            <div class="divTableCell" id="780">
                <div class="framenr">780</div>
                <div class="kanji">坂</div>
                <div class="keyword" style="display: none">slope</div>
            </div>

            <div class="divTableCell" id="781">
                <div class="framenr">781</div>
                <div class="kanji">板</div>
                <div class="keyword" style="display: none">plank</div>
            </div>

            <div class="divTableCell" id="782">
                <div class="framenr">782</div>
                <div class="kanji">返</div>
                <div class="keyword" style="display: none">return</div>
            </div>

            <div class="divTableCell" id="783">
                <div class="framenr">783</div>
                <div class="kanji">販</div>
                <div class="keyword" style="display: none">marketing</div>
            </div>

            <div class="divTableCell" id="784">
                <div class="framenr">784</div>
                <div class="kanji">爪</div>
                <div class="keyword" style="display: none">claw</div>
            </div>

            <div class="divTableCell" id="785">
                <div class="framenr">785</div>
                <div class="kanji">妥</div>
                <div class="keyword" style="display: none">gentle</div>
            </div>

            <div class="divTableCell" id="786">
                <div class="framenr">786</div>
                <div class="kanji">乳</div>
                <div class="keyword" style="display: none">milk</div>
            </div>

            <div class="divTableCell" id="787">
                <div class="framenr">787</div>
                <div class="kanji">浮</div>
                <div class="keyword" style="display: none">floating</div>
            </div>

            <div class="divTableCell" id="788">
                <div class="framenr">788</div>
                <div class="kanji">淫</div>
                <div class="keyword" style="display: none">lewd</div>
            </div>

            <div class="divTableCell" id="789">
                <div class="framenr">789</div>
                <div class="kanji">将</div>
                <div class="keyword" style="display: none">leader</div>
            </div>

            <div class="divTableCell" id="790">
                <div class="framenr">790</div>
                <div class="kanji">奨</div>
                <div class="keyword" style="display: none">exhort</div>
            </div>

            <div class="divTableCell" id="791">
                <div class="framenr">791</div>
                <div class="kanji">采</div>
                <div class="keyword" style="display: none">grab</div>
            </div>

            <div class="divTableCell" id="792">
                <div class="framenr">792</div>
                <div class="kanji">採</div>
                <div class="keyword" style="display: none">pick</div>
            </div>

            <div class="divTableCell" id="793">
                <div class="framenr">793</div>
                <div class="kanji">菜</div>
                <div class="keyword" style="display: none">vegetable</div>
            </div>

            <div class="divTableCell" id="794">
                <div class="framenr">794</div>
                <div class="kanji">受</div>
                <div class="keyword" style="display: none">accept</div>
            </div>

            <div class="divTableCell" id="795">
                <div class="framenr">795</div>
                <div class="kanji">授</div>
                <div class="keyword" style="display: none">impart</div>
            </div>

            <div class="divTableCell" id="796">
                <div class="framenr">796</div>
                <div class="kanji">愛</div>
                <div class="keyword" style="display: none">love</div>
            </div>

            <div class="divTableCell" id="797">
                <div class="framenr">797</div>
                <div class="kanji">曖</div>
                <div class="keyword" style="display: none">unclear</div>
            </div>

            <div class="divTableCell" id="798">
                <div class="framenr">798</div>
                <div class="kanji">払</div>
                <div class="keyword" style="display: none">pay</div>
            </div>

            <div class="divTableCell" id="799">
                <div class="framenr">799</div>
                <div class="kanji">広</div>
                <div class="keyword" style="display: none">wide</div>
            </div>

            <div class="divTableCell" id="800">
                <div class="framenr">800</div>
                <div class="kanji">勾</div>
                <div class="keyword" style="display: none">hooked</div>
            </div>

            <div class="divTableCell" id="801">
                <div class="framenr">801</div>
                <div class="kanji">拡</div>
                <div class="keyword" style="display: none">broaden</div>
            </div>

            <div class="divTableCell" id="802">
                <div class="framenr">802</div>
                <div class="kanji">鉱</div>
                <div class="keyword" style="display: none">mineral</div>
            </div>

            <div class="divTableCell" id="803">
                <div class="framenr">803</div>
                <div class="kanji">弁</div>
                <div class="keyword" style="display: none">valve</div>
            </div>

            <div class="divTableCell" id="804">
                <div class="framenr">804</div>
                <div class="kanji">雄</div>
                <div class="keyword" style="display: none">male</div>
            </div>

            <div class="divTableCell" id="805">
                <div class="framenr">805</div>
                <div class="kanji">台</div>
                <div class="keyword" style="display: none">pedestal</div>
            </div>

            <div class="divTableCell" id="806">
                <div class="framenr">806</div>
                <div class="kanji">怠</div>
                <div class="keyword" style="display: none">neglect</div>
            </div>

            <div class="divTableCell" id="807">
                <div class="framenr">807</div>
                <div class="kanji">治</div>
                <div class="keyword" style="display: none">reign</div>
            </div>

            <div class="divTableCell" id="808">
                <div class="framenr">808</div>
                <div class="kanji">冶</div>
                <div class="keyword" style="display: none">metallurgy</div>
            </div>

            <div class="divTableCell" id="809">
                <div class="framenr">809</div>
                <div class="kanji">始</div>
                <div class="keyword" style="display: none">commence</div>
            </div>

            <div class="divTableCell" id="810">
                <div class="framenr">810</div>
                <div class="kanji">胎</div>
                <div class="keyword" style="display: none">womb</div>
            </div>

            <div class="divTableCell" id="811">
                <div class="framenr">811</div>
                <div class="kanji">窓</div>
                <div class="keyword" style="display: none">window</div>
            </div>

            <div class="divTableCell" id="812">
                <div class="framenr">812</div>
                <div class="kanji">去</div>
                <div class="keyword" style="display: none">gone</div>
            </div>

            <div class="divTableCell" id="813">
                <div class="framenr">813</div>
                <div class="kanji">法</div>
                <div class="keyword" style="display: none">method</div>
            </div>

            <div class="divTableCell" id="814">
                <div class="framenr">814</div>
                <div class="kanji">会</div>
                <div class="keyword" style="display: none">meeting</div>
            </div>

            <div class="divTableCell" id="815">
                <div class="framenr">815</div>
                <div class="kanji">至</div>
                <div class="keyword" style="display: none">climax</div>
            </div>

            <div class="divTableCell" id="816">
                <div class="framenr">816</div>
                <div class="kanji">室</div>
                <div class="keyword" style="display: none">room</div>
            </div>

            <div class="divTableCell" id="817">
                <div class="framenr">817</div>
                <div class="kanji">到</div>
                <div class="keyword" style="display: none">arrival</div>
            </div>

            <div class="divTableCell" id="818">
                <div class="framenr">818</div>
                <div class="kanji">致</div>
                <div class="keyword" style="display: none">doth</div>
            </div>

            <div class="divTableCell" id="819">
                <div class="framenr">819</div>
                <div class="kanji">互</div>
                <div class="keyword" style="display: none">mutually</div>
            </div>

            <div class="divTableCell" id="820">
                <div class="framenr">820</div>
                <div class="kanji">棄</div>
                <div class="keyword" style="display: none">abandon</div>
            </div>

            <div class="divTableCell" id="821">
                <div class="framenr">821</div>
                <div class="kanji">育</div>
                <div class="keyword" style="display: none">bring up</div>
            </div>

            <div class="divTableCell" id="822">
                <div class="framenr">822</div>
                <div class="kanji">撤</div>
                <div class="keyword" style="display: none">remove</div>
            </div>

            <div class="divTableCell" id="823">
                <div class="framenr">823</div>
                <div class="kanji">充</div>
                <div class="keyword" style="display: none">allot</div>
            </div>

            <div class="divTableCell" id="824">
                <div class="framenr">824</div>
                <div class="kanji">銃</div>
                <div class="keyword" style="display: none">gun</div>
            </div>

            <div class="divTableCell" id="825">
                <div class="framenr">825</div>
                <div class="kanji">硫</div>
                <div class="keyword" style="display: none">sulfur</div>
            </div>

            <div class="divTableCell" id="826">
                <div class="framenr">826</div>
                <div class="kanji">流</div>
                <div class="keyword" style="display: none">current</div>
            </div>

            <div class="divTableCell" id="827">
                <div class="framenr">827</div>
                <div class="kanji">允</div>
                <div class="keyword" style="display: none">license</div>
            </div>

            <div class="divTableCell" id="828">
                <div class="framenr">828</div>
                <div class="kanji">唆</div>
                <div class="keyword" style="display: none">tempt</div>
            </div>

            <div class="divTableCell" id="829">
                <div class="framenr">829</div>
                <div class="kanji">出</div>
                <div class="keyword" style="display: none">exit</div>
            </div>

            <div class="divTableCell" id="830">
                <div class="framenr">830</div>
                <div class="kanji">山</div>
                <div class="keyword" style="display: none">mountain</div>
            </div>

            <div class="divTableCell" id="831">
                <div class="framenr">831</div>
                <div class="kanji">拙</div>
                <div class="keyword" style="display: none">bungling</div>
            </div>

            <div class="divTableCell" id="832">
                <div class="framenr">832</div>
                <div class="kanji">岩</div>
                <div class="keyword" style="display: none">boulder</div>
            </div>

            <div class="divTableCell" id="833">
                <div class="framenr">833</div>
                <div class="kanji">炭</div>
                <div class="keyword" style="display: none">charcoal</div>
            </div>

            <div class="divTableCell" id="834">
                <div class="framenr">834</div>
                <div class="kanji">岐</div>
                <div class="keyword" style="display: none">branch off</div>
            </div>

            <div class="divTableCell" id="835">
                <div class="framenr">835</div>
                <div class="kanji">峠</div>
                <div class="keyword" style="display: none">mountain pass</div>
            </div>

            <div class="divTableCell" id="836">
                <div class="framenr">836</div>
                <div class="kanji">崩</div>
                <div class="keyword" style="display: none">crumble</div>
            </div>

            <div class="divTableCell" id="837">
                <div class="framenr">837</div>
                <div class="kanji">密</div>
                <div class="keyword" style="display: none">secrecy</div>
            </div>

            <div class="divTableCell" id="838">
                <div class="framenr">838</div>
                <div class="kanji">蜜</div>
                <div class="keyword" style="display: none">honey</div>
            </div>

            <div class="divTableCell" id="839">
                <div class="framenr">839</div>
                <div class="kanji">嵐</div>
                <div class="keyword" style="display: none">storm</div>
            </div>

            <div class="divTableCell" id="840">
                <div class="framenr">840</div>
                <div class="kanji">崎</div>
                <div class="keyword" style="display: none">promontory</div>
            </div>

            <div class="divTableCell" id="841">
                <div class="framenr">841</div>
                <div class="kanji">崖</div>
                <div class="keyword" style="display: none">bluffs</div>
            </div>

            <div class="divTableCell" id="842">
                <div class="framenr">842</div>
                <div class="kanji">入</div>
                <div class="keyword" style="display: none">enter</div>
            </div>

            <div class="divTableCell" id="843">
                <div class="framenr">843</div>
                <div class="kanji">込</div>
                <div class="keyword" style="display: none">crowded</div>
            </div>

            <div class="divTableCell" id="844">
                <div class="framenr">844</div>
                <div class="kanji">分</div>
                <div class="keyword" style="display: none">part</div>
            </div>

            <div class="divTableCell" id="845">
                <div class="framenr">845</div>
                <div class="kanji">貧</div>
                <div class="keyword" style="display: none">poverty</div>
            </div>

            <div class="divTableCell" id="846">
                <div class="framenr">846</div>
                <div class="kanji">頒</div>
                <div class="keyword" style="display: none">partition</div>
            </div>

            <div class="divTableCell" id="847">
                <div class="framenr">847</div>
                <div class="kanji">公</div>
                <div class="keyword" style="display: none">public</div>
            </div>

            <div class="divTableCell" id="848">
                <div class="framenr">848</div>
                <div class="kanji">松</div>
                <div class="keyword" style="display: none">pine tree</div>
            </div>

            <div class="divTableCell" id="849">
                <div class="framenr">849</div>
                <div class="kanji">翁</div>
                <div class="keyword" style="display: none">venerable old man</div>
            </div>

            <div class="divTableCell" id="850">
                <div class="framenr">850</div>
                <div class="kanji">訟</div>
                <div class="keyword" style="display: none">sue</div>
            </div>

            <div class="divTableCell" id="851">
                <div class="framenr">851</div>
                <div class="kanji">谷</div>
                <div class="keyword" style="display: none">valley</div>
            </div>

            <div class="divTableCell" id="852">
                <div class="framenr">852</div>
                <div class="kanji">浴</div>
                <div class="keyword" style="display: none">bathe</div>
            </div>

            <div class="divTableCell" id="853">
                <div class="framenr">853</div>
                <div class="kanji">容</div>
                <div class="keyword" style="display: none">contain</div>
            </div>

            <div class="divTableCell" id="854">
                <div class="framenr">854</div>
                <div class="kanji">溶</div>
                <div class="keyword" style="display: none">melt</div>
            </div>

            <div class="divTableCell" id="855">
                <div class="framenr">855</div>
                <div class="kanji">欲</div>
                <div class="keyword" style="display: none">longing</div>
            </div>

            <div class="divTableCell" id="856">
                <div class="framenr">856</div>
                <div class="kanji">裕</div>
                <div class="keyword" style="display: none">abundant</div>
            </div>

            <div class="divTableCell" id="857">
                <div class="framenr">857</div>
                <div class="kanji">鉛</div>
                <div class="keyword" style="display: none">lead (metal)</div>
            </div>

            <div class="divTableCell" id="858">
                <div class="framenr">858</div>
                <div class="kanji">沿</div>
                <div class="keyword" style="display: none">run alongside</div>
            </div>

            <div class="divTableCell" id="859">
                <div class="framenr">859</div>
                <div class="kanji">賞</div>
                <div class="keyword" style="display: none">prize</div>
            </div>

            <div class="divTableCell" id="860">
                <div class="framenr">860</div>
                <div class="kanji">党</div>
                <div class="keyword" style="display: none">party</div>
            </div>

            <div class="divTableCell" id="861">
                <div class="framenr">861</div>
                <div class="kanji">堂</div>
                <div class="keyword" style="display: none">hall</div>
            </div>

            <div class="divTableCell" id="862">
                <div class="framenr">862</div>
                <div class="kanji">常</div>
                <div class="keyword" style="display: none">usual</div>
            </div>

            <div class="divTableCell" id="863">
                <div class="framenr">863</div>
                <div class="kanji">裳</div>
                <div class="keyword" style="display: none">skirt</div>
            </div>

            <div class="divTableCell" id="864">
                <div class="framenr">864</div>
                <div class="kanji">掌</div>
                <div class="keyword" style="display: none">manipulate</div>
            </div>

            <div class="divTableCell" id="865">
                <div class="framenr">865</div>
                <div class="kanji">皮</div>
                <div class="keyword" style="display: none">pelt</div>
            </div>

            <div class="divTableCell" id="866">
                <div class="framenr">866</div>
                <div class="kanji">波</div>
                <div class="keyword" style="display: none">waves</div>
            </div>

            <div class="divTableCell" id="867">
                <div class="framenr">867</div>
                <div class="kanji">婆</div>
                <div class="keyword" style="display: none">old woman</div>
            </div>

            <div class="divTableCell" id="868">
                <div class="framenr">868</div>
                <div class="kanji">披</div>
                <div class="keyword" style="display: none">expose</div>
            </div>

            <div class="divTableCell" id="869">
                <div class="framenr">869</div>
                <div class="kanji">破</div>
                <div class="keyword" style="display: none">rend</div>
            </div>

            <div class="divTableCell" id="870">
                <div class="framenr">870</div>
                <div class="kanji">被</div>
                <div class="keyword" style="display: none">incur</div>
            </div>

            <div class="divTableCell" id="871">
                <div class="framenr">871</div>
                <div class="kanji">残</div>
                <div class="keyword" style="display: none">remainder</div>
            </div>

            <div class="divTableCell" id="872">
                <div class="framenr">872</div>
                <div class="kanji">殉</div>
                <div class="keyword" style="display: none">martyrdom</div>
            </div>

            <div class="divTableCell" id="873">
                <div class="framenr">873</div>
                <div class="kanji">殊</div>
                <div class="keyword" style="display: none">particularly</div>
            </div>

            <div class="divTableCell" id="874">
                <div class="framenr">874</div>
                <div class="kanji">殖</div>
                <div class="keyword" style="display: none">augment</div>
            </div>

            <div class="divTableCell" id="875">
                <div class="framenr">875</div>
                <div class="kanji">列</div>
                <div class="keyword" style="display: none">file</div>
            </div>

            <div class="divTableCell" id="876">
                <div class="framenr">876</div>
                <div class="kanji">裂</div>
                <div class="keyword" style="display: none">split</div>
            </div>

            <div class="divTableCell" id="877">
                <div class="framenr">877</div>
                <div class="kanji">烈</div>
                <div class="keyword" style="display: none">ardent</div>
            </div>

            <div class="divTableCell" id="878">
                <div class="framenr">878</div>
                <div class="kanji">死</div>
                <div class="keyword" style="display: none">death</div>
            </div>

            <div class="divTableCell" id="879">
                <div class="framenr">879</div>
                <div class="kanji">葬</div>
                <div class="keyword" style="display: none">interment</div>
            </div>

            <div class="divTableCell" id="880">
                <div class="framenr">880</div>
                <div class="kanji">瞬</div>
                <div class="keyword" style="display: none">wink</div>
            </div>

            <div class="divTableCell" id="881">
                <div class="framenr">881</div>
                <div class="kanji">耳</div>
                <div class="keyword" style="display: none">ear</div>
            </div>

            <div class="divTableCell" id="882">
                <div class="framenr">882</div>
                <div class="kanji">取</div>
                <div class="keyword" style="display: none">take</div>
            </div>

            <div class="divTableCell" id="883">
                <div class="framenr">883</div>
                <div class="kanji">趣</div>
                <div class="keyword" style="display: none">gist</div>
            </div>

            <div class="divTableCell" id="884">
                <div class="framenr">884</div>
                <div class="kanji">最</div>
                <div class="keyword" style="display: none">utmost</div>
            </div>

            <div class="divTableCell" id="885">
                <div class="framenr">885</div>
                <div class="kanji">撮</div>
                <div class="keyword" style="display: none">snapshot</div>
            </div>

            <div class="divTableCell" id="886">
                <div class="framenr">886</div>
                <div class="kanji">恥</div>
                <div class="keyword" style="display: none">shame</div>
            </div>

            <div class="divTableCell" id="887">
                <div class="framenr">887</div>
                <div class="kanji">職</div>
                <div class="keyword" style="display: none">post</div>
            </div>

            <div class="divTableCell" id="888">
                <div class="framenr">888</div>
                <div class="kanji">聖</div>
                <div class="keyword" style="display: none">holy</div>
            </div>

            <div class="divTableCell" id="889">
                <div class="framenr">889</div>
                <div class="kanji">敢</div>
                <div class="keyword" style="display: none">daring</div>
            </div>

            <div class="divTableCell" id="890">
                <div class="framenr">890</div>
                <div class="kanji">聴</div>
                <div class="keyword" style="display: none">listen</div>
            </div>

            <div class="divTableCell" id="891">
                <div class="framenr">891</div>
                <div class="kanji">懐</div>
                <div class="keyword" style="display: none">pocket</div>
            </div>

            <div class="divTableCell" id="892">
                <div class="framenr">892</div>
                <div class="kanji">慢</div>
                <div class="keyword" style="display: none">ridicule(mandala)</div>
            </div>

            <div class="divTableCell" id="893">
                <div class="framenr">893</div>
                <div class="kanji">漫</div>
                <div class="keyword" style="display: none">loose(manga)</div>
            </div>

            <div class="divTableCell" id="894">
                <div class="framenr">894</div>
                <div class="kanji">買</div>
                <div class="keyword" style="display: none">buy</div>
            </div>

            <div class="divTableCell" id="895">
                <div class="framenr">895</div>
                <div class="kanji">置</div>
                <div class="keyword" style="display: none">placement</div>
            </div>

            <div class="divTableCell" id="896">
                <div class="framenr">896</div>
                <div class="kanji">罰</div>
                <div class="keyword" style="display: none">penalty</div>
            </div>

            <div class="divTableCell" id="897">
                <div class="framenr">897</div>
                <div class="kanji">寧</div>
                <div class="keyword" style="display: none">rather</div>
            </div>

            <div class="divTableCell" id="898">
                <div class="framenr">898</div>
                <div class="kanji">濁</div>
                <div class="keyword" style="display: none">voiced</div>
            </div>

            <div class="divTableCell" id="899">
                <div class="framenr">899</div>
                <div class="kanji">環</div>
                <div class="keyword" style="display: none">ring</div>
            </div>

            <div class="divTableCell" id="900">
                <div class="framenr">900</div>
                <div class="kanji">還</div>
                <div class="keyword" style="display: none">send back</div>
            </div>

            <div class="divTableCell" id="901">
                <div class="framenr">901</div>
                <div class="kanji">夫</div>
                <div class="keyword" style="display: none">husband</div>
            </div>

            <div class="divTableCell" id="902">
                <div class="framenr">902</div>
                <div class="kanji">扶</div>
                <div class="keyword" style="display: none">aid</div>
            </div>

            <div class="divTableCell" id="903">
                <div class="framenr">903</div>
                <div class="kanji">渓</div>
                <div class="keyword" style="display: none">mountain stream</div>
            </div>

            <div class="divTableCell" id="904">
                <div class="framenr">904</div>
                <div class="kanji">規</div>
                <div class="keyword" style="display: none">standard</div>
            </div>

            <div class="divTableCell" id="905">
                <div class="framenr">905</div>
                <div class="kanji">替</div>
                <div class="keyword" style="display: none">exchange</div>
            </div>

            <div class="divTableCell" id="906">
                <div class="framenr">906</div>
                <div class="kanji">賛</div>
                <div class="keyword" style="display: none">approve</div>
            </div>

            <div class="divTableCell" id="907">
                <div class="framenr">907</div>
                <div class="kanji">潜</div>
                <div class="keyword" style="display: none">submerge</div>
            </div>

            <div class="divTableCell" id="908">
                <div class="framenr">908</div>
                <div class="kanji">失</div>
                <div class="keyword" style="display: none">lose</div>
            </div>

            <div class="divTableCell" id="909">
                <div class="framenr">909</div>
                <div class="kanji">鉄</div>
                <div class="keyword" style="display: none">iron</div>
            </div>

            <div class="divTableCell" id="910">
                <div class="framenr">910</div>
                <div class="kanji">迭</div>
                <div class="keyword" style="display: none">alternate</div>
            </div>

            <div class="divTableCell" id="911">
                <div class="framenr">911</div>
                <div class="kanji">臣</div>
                <div class="keyword" style="display: none">retainer</div>
            </div>

            <div class="divTableCell" id="912">
                <div class="framenr">912</div>
                <div class="kanji">姫</div>
                <div class="keyword" style="display: none">princess</div>
            </div>

            <div class="divTableCell" id="913">
                <div class="framenr">913</div>
                <div class="kanji">蔵</div>
                <div class="keyword" style="display: none">storehouse</div>
            </div>

            <div class="divTableCell" id="914">
                <div class="framenr">914</div>
                <div class="kanji">臓</div>
                <div class="keyword" style="display: none">entrails</div>
            </div>

            <div class="divTableCell" id="915">
                <div class="framenr">915</div>
                <div class="kanji">賢</div>
                <div class="keyword" style="display: none">intelligent</div>
            </div>

            <div class="divTableCell" id="916">
                <div class="framenr">916</div>
                <div class="kanji">腎</div>
                <div class="keyword" style="display: none">kidney</div>
            </div>

            <div class="divTableCell" id="917">
                <div class="framenr">917</div>
                <div class="kanji">堅</div>
                <div class="keyword" style="display: none">strict</div>
            </div>

            <div class="divTableCell" id="918">
                <div class="framenr">918</div>
                <div class="kanji">臨</div>
                <div class="keyword" style="display: none">look to</div>
            </div>

            <div class="divTableCell" id="919">
                <div class="framenr">919</div>
                <div class="kanji">覧</div>
                <div class="keyword" style="display: none">perusal</div>
            </div>

            <div class="divTableCell" id="920">
                <div class="framenr">920</div>
                <div class="kanji">巨</div>
                <div class="keyword" style="display: none">gigantic</div>
            </div>

            <div class="divTableCell" id="921">
                <div class="framenr">921</div>
                <div class="kanji">拒</div>
                <div class="keyword" style="display: none">repel</div>
            </div>

            <div class="divTableCell" id="922">
                <div class="framenr">922</div>
                <div class="kanji">力</div>
                <div class="keyword" style="display: none">power</div>
            </div>

            <div class="divTableCell" id="923">
                <div class="framenr">923</div>
                <div class="kanji">男</div>
                <div class="keyword" style="display: none">man</div>
            </div>

            <div class="divTableCell" id="924">
                <div class="framenr">924</div>
                <div class="kanji">労</div>
                <div class="keyword" style="display: none">labor</div>
            </div>

            <div class="divTableCell" id="925">
                <div class="framenr">925</div>
                <div class="kanji">募</div>
                <div class="keyword" style="display: none">recruit</div>
            </div>

            <div class="divTableCell" id="926">
                <div class="framenr">926</div>
                <div class="kanji">劣</div>
                <div class="keyword" style="display: none">inferiority</div>
            </div>

            <div class="divTableCell" id="927">
                <div class="framenr">927</div>
                <div class="kanji">功</div>
                <div class="keyword" style="display: none">achievement</div>
            </div>

            <div class="divTableCell" id="928">
                <div class="framenr">928</div>
                <div class="kanji">勧</div>
                <div class="keyword" style="display: none">persuade</div>
            </div>

            <div class="divTableCell" id="929">
                <div class="framenr">929</div>
                <div class="kanji">努</div>
                <div class="keyword" style="display: none">toil</div>
            </div>

            <div class="divTableCell" id="930">
                <div class="framenr">930</div>
                <div class="kanji">勃</div>
                <div class="keyword" style="display: none">uprising,suddenness</div>
            </div>

            <div class="divTableCell" id="931">
                <div class="framenr">931</div>
                <div class="kanji">励</div>
                <div class="keyword" style="display: none">encourage</div>
            </div>

            <div class="divTableCell" id="932">
                <div class="framenr">932</div>
                <div class="kanji">加</div>
                <div class="keyword" style="display: none">add</div>
            </div>

            <div class="divTableCell" id="933">
                <div class="framenr">933</div>
                <div class="kanji">賀</div>
                <div class="keyword" style="display: none">congratulations</div>
            </div>

            <div class="divTableCell" id="934">
                <div class="framenr">934</div>
                <div class="kanji">架</div>
                <div class="keyword" style="display: none">erect</div>
            </div>

            <div class="divTableCell" id="935">
                <div class="framenr">935</div>
                <div class="kanji">脇</div>
                <div class="keyword" style="display: none">armpit</div>
            </div>

            <div class="divTableCell" id="936">
                <div class="framenr">936</div>
                <div class="kanji">脅</div>
                <div class="keyword" style="display: none">threaten</div>
            </div>

            <div class="divTableCell" id="937">
                <div class="framenr">937</div>
                <div class="kanji">協</div>
                <div class="keyword" style="display: none">co-</div>
            </div>

            <div class="divTableCell" id="938">
                <div class="framenr">938</div>
                <div class="kanji">行</div>
                <div class="keyword" style="display: none">going</div>
            </div>

            <div class="divTableCell" id="939">
                <div class="framenr">939</div>
                <div class="kanji">律</div>
                <div class="keyword" style="display: none">rhythm</div>
            </div>

            <div class="divTableCell" id="940">
                <div class="framenr">940</div>
                <div class="kanji">復</div>
                <div class="keyword" style="display: none">restore</div>
            </div>

            <div class="divTableCell" id="941">
                <div class="framenr">941</div>
                <div class="kanji">得</div>
                <div class="keyword" style="display: none">gain</div>
            </div>

            <div class="divTableCell" id="942">
                <div class="framenr">942</div>
                <div class="kanji">従</div>
                <div class="keyword" style="display: none">accompany</div>
            </div>

            <div class="divTableCell" id="943">
                <div class="framenr">943</div>
                <div class="kanji">徒</div>
                <div class="keyword" style="display: none">junior</div>
            </div>

            <div class="divTableCell" id="944">
                <div class="framenr">944</div>
                <div class="kanji">待</div>
                <div class="keyword" style="display: none">wait</div>
            </div>

            <div class="divTableCell" id="945">
                <div class="framenr">945</div>
                <div class="kanji">往</div>
                <div class="keyword" style="display: none">journey</div>
            </div>

            <div class="divTableCell" id="946">
                <div class="framenr">946</div>
                <div class="kanji">征</div>
                <div class="keyword" style="display: none">subjugate</div>
            </div>

            <div class="divTableCell" id="947">
                <div class="framenr">947</div>
                <div class="kanji">径</div>
                <div class="keyword" style="display: none">diameter</div>
            </div>

            <div class="divTableCell" id="948">
                <div class="framenr">948</div>
                <div class="kanji">彼</div>
                <div class="keyword" style="display: none">he</div>
            </div>

            <div class="divTableCell" id="949">
                <div class="framenr">949</div>
                <div class="kanji">役</div>
                <div class="keyword" style="display: none">duty</div>
            </div>

            <div class="divTableCell" id="950">
                <div class="framenr">950</div>
                <div class="kanji">徳</div>
                <div class="keyword" style="display: none">benevolence</div>
            </div>

            <div class="divTableCell" id="951">
                <div class="framenr">951</div>
                <div class="kanji">徹</div>
                <div class="keyword" style="display: none">penetrate</div>
            </div>

            <div class="divTableCell" id="952">
                <div class="framenr">952</div>
                <div class="kanji">徴</div>
                <div class="keyword" style="display: none">indications</div>
            </div>

            <div class="divTableCell" id="953">
                <div class="framenr">953</div>
                <div class="kanji">懲</div>
                <div class="keyword" style="display: none">penal</div>
            </div>

            <div class="divTableCell" id="954">
                <div class="framenr">954</div>
                <div class="kanji">微</div>
                <div class="keyword" style="display: none">delicate</div>
            </div>

            <div class="divTableCell" id="955">
                <div class="framenr">955</div>
                <div class="kanji">街</div>
                <div class="keyword" style="display: none">boulevard</div>
            </div>

            <div class="divTableCell" id="956">
                <div class="framenr">956</div>
                <div class="kanji">桁</div>
                <div class="keyword" style="display: none">girder</div>
            </div>

            <div class="divTableCell" id="957">
                <div class="framenr">957</div>
                <div class="kanji">衡</div>
                <div class="keyword" style="display: none">equilibrium</div>
            </div>

            <div class="divTableCell" id="958">
                <div class="framenr">958</div>
                <div class="kanji">稿</div>
                <div class="keyword" style="display: none">draft</div>
            </div>

            <div class="divTableCell" id="959">
                <div class="framenr">959</div>
                <div class="kanji">稼</div>
                <div class="keyword" style="display: none">earnings</div>
            </div>

            <div class="divTableCell" id="960">
                <div class="framenr">960</div>
                <div class="kanji">程</div>
                <div class="keyword" style="display: none">extent</div>
            </div>

            <div class="divTableCell" id="961">
                <div class="framenr">961</div>
                <div class="kanji">税</div>
                <div class="keyword" style="display: none">tax</div>
            </div>

            <div class="divTableCell" id="962">
                <div class="framenr">962</div>
                <div class="kanji">稚</div>
                <div class="keyword" style="display: none">immature</div>
            </div>

            <div class="divTableCell" id="963">
                <div class="framenr">963</div>
                <div class="kanji">和</div>
                <div class="keyword" style="display: none">harmony</div>
            </div>

            <div class="divTableCell" id="964">
                <div class="framenr">964</div>
                <div class="kanji">移</div>
                <div class="keyword" style="display: none">shift</div>
            </div>

            <div class="divTableCell" id="965">
                <div class="framenr">965</div>
                <div class="kanji">秒</div>
                <div class="keyword" style="display: none">second</div>
            </div>

            <div class="divTableCell" id="966">
                <div class="framenr">966</div>
                <div class="kanji">秋</div>
                <div class="keyword" style="display: none">autumn</div>
            </div>

            <div class="divTableCell" id="967">
                <div class="framenr">967</div>
                <div class="kanji">愁</div>
                <div class="keyword" style="display: none">distress</div>
            </div>

            <div class="divTableCell" id="968">
                <div class="framenr">968</div>
                <div class="kanji">私</div>
                <div class="keyword" style="display: none">private</div>
            </div>

            <div class="divTableCell" id="969">
                <div class="framenr">969</div>
                <div class="kanji">秩</div>
                <div class="keyword" style="display: none">regularity</div>
            </div>

            <div class="divTableCell" id="970">
                <div class="framenr">970</div>
                <div class="kanji">秘</div>
                <div class="keyword" style="display: none">secret</div>
            </div>

            <div class="divTableCell" id="971">
                <div class="framenr">971</div>
                <div class="kanji">称</div>
                <div class="keyword" style="display: none">appellation</div>
            </div>

            <div class="divTableCell" id="972">
                <div class="framenr">972</div>
                <div class="kanji">利</div>
                <div class="keyword" style="display: none">profit</div>
            </div>

            <div class="divTableCell" id="973">
                <div class="framenr">973</div>
                <div class="kanji">梨</div>
                <div class="keyword" style="display: none">pear tree</div>
            </div>

            <div class="divTableCell" id="974">
                <div class="framenr">974</div>
                <div class="kanji">穫</div>
                <div class="keyword" style="display: none">harvest</div>
            </div>

            <div class="divTableCell" id="975">
                <div class="framenr">975</div>
                <div class="kanji">穂</div>
                <div class="keyword" style="display: none">ear of a plant</div>
            </div>

            <div class="divTableCell" id="976">
                <div class="framenr">976</div>
                <div class="kanji">稲</div>
                <div class="keyword" style="display: none">rice plant</div>
            </div>

            <div class="divTableCell" id="977">
                <div class="framenr">977</div>
                <div class="kanji">香</div>
                <div class="keyword" style="display: none">incense</div>
            </div>

            <div class="divTableCell" id="978">
                <div class="framenr">978</div>
                <div class="kanji">季</div>
                <div class="keyword" style="display: none">seasons</div>
            </div>

            <div class="divTableCell" id="979">
                <div class="framenr">979</div>
                <div class="kanji">委</div>
                <div class="keyword" style="display: none">committee</div>
            </div>

            <div class="divTableCell" id="980">
                <div class="framenr">980</div>
                <div class="kanji">秀</div>
                <div class="keyword" style="display: none">excel</div>
            </div>

            <div class="divTableCell" id="981">
                <div class="framenr">981</div>
                <div class="kanji">透</div>
                <div class="keyword" style="display: none">transparent</div>
            </div>

            <div class="divTableCell" id="982">
                <div class="framenr">982</div>
                <div class="kanji">誘</div>
                <div class="keyword" style="display: none">entice</div>
            </div>

            <div class="divTableCell" id="983">
                <div class="framenr">983</div>
                <div class="kanji">稽</div>
                <div class="keyword" style="display: none">training</div>
            </div>

            <div class="divTableCell" id="984">
                <div class="framenr">984</div>
                <div class="kanji">穀</div>
                <div class="keyword" style="display: none">cereals</div>
            </div>

            <div class="divTableCell" id="985">
                <div class="framenr">985</div>
                <div class="kanji">菌</div>
                <div class="keyword" style="display: none">germ</div>
            </div>

            <div class="divTableCell" id="986">
                <div class="framenr">986</div>
                <div class="kanji">萎</div>
                <div class="keyword" style="display: none">numb(fade away)</div>
            </div>

            <div class="divTableCell" id="987">
                <div class="framenr">987</div>
                <div class="kanji">米</div>
                <div class="keyword" style="display: none">rice</div>
            </div>

            <div class="divTableCell" id="988">
                <div class="framenr">988</div>
                <div class="kanji">粉</div>
                <div class="keyword" style="display: none">flour</div>
            </div>

            <div class="divTableCell" id="989">
                <div class="framenr">989</div>
                <div class="kanji">粘</div>
                <div class="keyword" style="display: none">sticky</div>
            </div>

            <div class="divTableCell" id="990">
                <div class="framenr">990</div>
                <div class="kanji">粒</div>
                <div class="keyword" style="display: none">grains</div>
            </div>

            <div class="divTableCell" id="991">
                <div class="framenr">991</div>
                <div class="kanji">粧</div>
                <div class="keyword" style="display: none">cosmetics</div>
            </div>

            <div class="divTableCell" id="992">
                <div class="framenr">992</div>
                <div class="kanji">迷</div>
                <div class="keyword" style="display: none">astray</div>
            </div>

            <div class="divTableCell" id="993">
                <div class="framenr">993</div>
                <div class="kanji">粋</div>
                <div class="keyword" style="display: none">chic</div>
            </div>

            <div class="divTableCell" id="994">
                <div class="framenr">994</div>
                <div class="kanji">謎</div>
                <div class="keyword" style="display: none">riddle</div>
            </div>

            <div class="divTableCell" id="995">
                <div class="framenr">995</div>
                <div class="kanji">糧</div>
                <div class="keyword" style="display: none">provisions</div>
            </div>

            <div class="divTableCell" id="996">
                <div class="framenr">996</div>
                <div class="kanji">菊</div>
                <div class="keyword" style="display: none">chrysanthemum</div>
            </div>

            <div class="divTableCell" id="997">
                <div class="framenr">997</div>
                <div class="kanji">奥</div>
                <div class="keyword" style="display: none">core</div>
            </div>

            <div class="divTableCell" id="998">
                <div class="framenr">998</div>
                <div class="kanji">数</div>
                <div class="keyword" style="display: none">number</div>
            </div>

            <div class="divTableCell" id="999">
                <div class="framenr">999</div>
                <div class="kanji">楼</div>
                <div class="keyword" style="display: none">watchtower</div>
            </div>

            <div class="divTableCell" id="1000">
                <div class="framenr">1000</div>
                <div class="kanji">類</div>
                <div class="keyword" style="display: none">sort</div>
            </div>

            <div class="divTableCell" id="1001">
                <div class="framenr">1001</div>
                <div class="kanji">漆</div>
                <div class="keyword" style="display: none">lacquer</div>
            </div>

            <div class="divTableCell" id="1002">
                <div class="framenr">1002</div>
                <div class="kanji">膝</div>
                <div class="keyword" style="display: none">knee</div>
            </div>

            <div class="divTableCell" id="1003">
                <div class="framenr">1003</div>
                <div class="kanji">様</div>
                <div class="keyword" style="display: none">Esq.</div>
            </div>

            <div class="divTableCell" id="1004">
                <div class="framenr">1004</div>
                <div class="kanji">求</div>
                <div class="keyword" style="display: none">request</div>
            </div>

            <div class="divTableCell" id="1005">
                <div class="framenr">1005</div>
                <div class="kanji">球</div>
                <div class="keyword" style="display: none">ball</div>
            </div>

            <div class="divTableCell" id="1006">
                <div class="framenr">1006</div>
                <div class="kanji">救</div>
                <div class="keyword" style="display: none">salvation</div>
            </div>

            <div class="divTableCell" id="1007">
                <div class="framenr">1007</div>
                <div class="kanji">竹</div>
                <div class="keyword" style="display: none">bamboo</div>
            </div>

            <div class="divTableCell" id="1008">
                <div class="framenr">1008</div>
                <div class="kanji">笑</div>
                <div class="keyword" style="display: none">laugh</div>
            </div>

            <div class="divTableCell" id="1009">
                <div class="framenr">1009</div>
                <div class="kanji">笠</div>
                <div class="keyword" style="display: none">bamboo hat</div>
            </div>

            <div class="divTableCell" id="1010">
                <div class="framenr">1010</div>
                <div class="kanji">笹</div>
                <div class="keyword" style="display: none">bamboo grass</div>
            </div>

            <div class="divTableCell" id="1011">
                <div class="framenr">1011</div>
                <div class="kanji">箋</div>
                <div class="keyword" style="display: none">stationery</div>
            </div>

            <div class="divTableCell" id="1012">
                <div class="framenr">1012</div>
                <div class="kanji">筋</div>
                <div class="keyword" style="display: none">muscle</div>
            </div>

            <div class="divTableCell" id="1013">
                <div class="framenr">1013</div>
                <div class="kanji">箱</div>
                <div class="keyword" style="display: none">box</div>
            </div>

            <div class="divTableCell" id="1014">
                <div class="framenr">1014</div>
                <div class="kanji">筆</div>
                <div class="keyword" style="display: none">writing brush</div>
            </div>

            <div class="divTableCell" id="1015">
                <div class="framenr">1015</div>
                <div class="kanji">筒</div>
                <div class="keyword" style="display: none">cylinder</div>
            </div>

            <div class="divTableCell" id="1016">
                <div class="framenr">1016</div>
                <div class="kanji">等</div>
                <div class="keyword" style="display: none">etc.</div>
            </div>

            <div class="divTableCell" id="1017">
                <div class="framenr">1017</div>
                <div class="kanji">算</div>
                <div class="keyword" style="display: none">calculate</div>
            </div>

            <div class="divTableCell" id="1018">
                <div class="framenr">1018</div>
                <div class="kanji">答</div>
                <div class="keyword" style="display: none">solution</div>
            </div>

            <div class="divTableCell" id="1019">
                <div class="framenr">1019</div>
                <div class="kanji">策</div>
                <div class="keyword" style="display: none">scheme</div>
            </div>

            <div class="divTableCell" id="1020">
                <div class="framenr">1020</div>
                <div class="kanji">簿</div>
                <div class="keyword" style="display: none">register</div>
            </div>

            <div class="divTableCell" id="1021">
                <div class="framenr">1021</div>
                <div class="kanji">築</div>
                <div class="keyword" style="display: none">fabricate</div>
            </div>

            <div class="divTableCell" id="1022">
                <div class="framenr">1022</div>
                <div class="kanji">篭</div>
                <div class="keyword" style="display: none">basket</div>
            </div>

            <div class="divTableCell" id="1023">
                <div class="framenr">1023</div>
                <div class="kanji">人</div>
                <div class="keyword" style="display: none">person</div>
            </div>

            <div class="divTableCell" id="1024">
                <div class="framenr">1024</div>
                <div class="kanji">佐</div>
                <div class="keyword" style="display: none">assistant</div>
            </div>

            <div class="divTableCell" id="1025">
                <div class="framenr">1025</div>
                <div class="kanji">侶</div>
                <div class="keyword" style="display: none">partner,follower</div>
            </div>

            <div class="divTableCell" id="1026">
                <div class="framenr">1026</div>
                <div class="kanji">但</div>
                <div class="keyword" style="display: none">however</div>
            </div>

            <div class="divTableCell" id="1027">
                <div class="framenr">1027</div>
                <div class="kanji">住</div>
                <div class="keyword" style="display: none">dwell</div>
            </div>

            <div class="divTableCell" id="1028">
                <div class="framenr">1028</div>
                <div class="kanji">位</div>
                <div class="keyword" style="display: none">rank</div>
            </div>

            <div class="divTableCell" id="1029">
                <div class="framenr">1029</div>
                <div class="kanji">仲</div>
                <div class="keyword" style="display: none">go-between</div>
            </div>

            <div class="divTableCell" id="1030">
                <div class="framenr">1030</div>
                <div class="kanji">体</div>
                <div class="keyword" style="display: none">body</div>
            </div>

            <div class="divTableCell" id="1031">
                <div class="framenr">1031</div>
                <div class="kanji">悠</div>
                <div class="keyword" style="display: none">remote</div>
            </div>

            <div class="divTableCell" id="1032">
                <div class="framenr">1032</div>
                <div class="kanji">件</div>
                <div class="keyword" style="display: none">affair</div>
            </div>

            <div class="divTableCell" id="1033">
                <div class="framenr">1033</div>
                <div class="kanji">仕</div>
                <div class="keyword" style="display: none">attend</div>
            </div>

            <div class="divTableCell" id="1034">
                <div class="framenr">1034</div>
                <div class="kanji">他</div>
                <div class="keyword" style="display: none">other</div>
            </div>

            <div class="divTableCell" id="1035">
                <div class="framenr">1035</div>
                <div class="kanji">伏</div>
                <div class="keyword" style="display: none">prostrated</div>
            </div>

            <div class="divTableCell" id="1036">
                <div class="framenr">1036</div>
                <div class="kanji">伝</div>
                <div class="keyword" style="display: none">transmit</div>
            </div>

            <div class="divTableCell" id="1037">
                <div class="framenr">1037</div>
                <div class="kanji">仏</div>
                <div class="keyword" style="display: none">Buddha</div>
            </div>

            <div class="divTableCell" id="1038">
                <div class="framenr">1038</div>
                <div class="kanji">休</div>
                <div class="keyword" style="display: none">rest</div>
            </div>

            <div class="divTableCell" id="1039">
                <div class="framenr">1039</div>
                <div class="kanji">仮</div>
                <div class="keyword" style="display: none">provisional</div>
            </div>

            <div class="divTableCell" id="1040">
                <div class="framenr">1040</div>
                <div class="kanji">伎</div>
                <div class="keyword" style="display: none">performing artist</div>
            </div>

            <div class="divTableCell" id="1041">
                <div class="framenr">1041</div>
                <div class="kanji">伯</div>
                <div class="keyword" style="display: none">chief</div>
            </div>

            <div class="divTableCell" id="1042">
                <div class="framenr">1042</div>
                <div class="kanji">俗</div>
                <div class="keyword" style="display: none">vulgar</div>
            </div>

            <div class="divTableCell" id="1043">
                <div class="framenr">1043</div>
                <div class="kanji">信</div>
                <div class="keyword" style="display: none">faith</div>
            </div>

            <div class="divTableCell" id="1044">
                <div class="framenr">1044</div>
                <div class="kanji">佳</div>
                <div class="keyword" style="display: none">excellent</div>
            </div>

            <div class="divTableCell" id="1045">
                <div class="framenr">1045</div>
                <div class="kanji">依</div>
                <div class="keyword" style="display: none">reliant</div>
            </div>

            <div class="divTableCell" id="1046">
                <div class="framenr">1046</div>
                <div class="kanji">例</div>
                <div class="keyword" style="display: none">example</div>
            </div>

            <div class="divTableCell" id="1047">
                <div class="framenr">1047</div>
                <div class="kanji">個</div>
                <div class="keyword" style="display: none">individual</div>
            </div>

            <div class="divTableCell" id="1048">
                <div class="framenr">1048</div>
                <div class="kanji">健</div>
                <div class="keyword" style="display: none">healthy</div>
            </div>

            <div class="divTableCell" id="1049">
                <div class="framenr">1049</div>
                <div class="kanji">側</div>
                <div class="keyword" style="display: none">side</div>
            </div>

            <div class="divTableCell" id="1050">
                <div class="framenr">1050</div>
                <div class="kanji">侍</div>
                <div class="keyword" style="display: none">waiter</div>
            </div>

            <div class="divTableCell" id="1051">
                <div class="framenr">1051</div>
                <div class="kanji">停</div>
                <div class="keyword" style="display: none">halt</div>
            </div>

            <div class="divTableCell" id="1052">
                <div class="framenr">1052</div>
                <div class="kanji">値</div>
                <div class="keyword" style="display: none">price</div>
            </div>

            <div class="divTableCell" id="1053">
                <div class="framenr">1053</div>
                <div class="kanji">倣</div>
                <div class="keyword" style="display: none">emulate</div>
            </div>

            <div class="divTableCell" id="1054">
                <div class="framenr">1054</div>
                <div class="kanji">傲</div>
                <div class="keyword" style="display: none">arrogance</div>
            </div>

            <div class="divTableCell" id="1055">
                <div class="framenr">1055</div>
                <div class="kanji">倒</div>
                <div class="keyword" style="display: none">overthrow</div>
            </div>

            <div class="divTableCell" id="1056">
                <div class="framenr">1056</div>
                <div class="kanji">偵</div>
                <div class="keyword" style="display: none">spy</div>
            </div>

            <div class="divTableCell" id="1057">
                <div class="framenr">1057</div>
                <div class="kanji">僧</div>
                <div class="keyword" style="display: none">Buddhist priest</div>
            </div>

            <div class="divTableCell" id="1058">
                <div class="framenr">1058</div>
                <div class="kanji">億</div>
                <div class="keyword" style="display: none">hundred million</div>
            </div>

            <div class="divTableCell" id="1059">
                <div class="framenr">1059</div>
                <div class="kanji">儀</div>
                <div class="keyword" style="display: none">ceremony</div>
            </div>

            <div class="divTableCell" id="1060">
                <div class="framenr">1060</div>
                <div class="kanji">償</div>
                <div class="keyword" style="display: none">reparation</div>
            </div>

            <div class="divTableCell" id="1061">
                <div class="framenr">1061</div>
                <div class="kanji">仙</div>
                <div class="keyword" style="display: none">hermit</div>
            </div>

            <div class="divTableCell" id="1062">
                <div class="framenr">1062</div>
                <div class="kanji">催</div>
                <div class="keyword" style="display: none">sponsor</div>
            </div>

            <div class="divTableCell" id="1063">
                <div class="framenr">1063</div>
                <div class="kanji">仁</div>
                <div class="keyword" style="display: none">humanity</div>
            </div>

            <div class="divTableCell" id="1064">
                <div class="framenr">1064</div>
                <div class="kanji">侮</div>
                <div class="keyword" style="display: none">scorn</div>
            </div>

            <div class="divTableCell" id="1065">
                <div class="framenr">1065</div>
                <div class="kanji">使</div>
                <div class="keyword" style="display: none">use</div>
            </div>

            <div class="divTableCell" id="1066">
                <div class="framenr">1066</div>
                <div class="kanji">便</div>
                <div class="keyword" style="display: none">convenience</div>
            </div>

            <div class="divTableCell" id="1067">
                <div class="framenr">1067</div>
                <div class="kanji">倍</div>
                <div class="keyword" style="display: none">double</div>
            </div>

            <div class="divTableCell" id="1068">
                <div class="framenr">1068</div>
                <div class="kanji">優</div>
                <div class="keyword" style="display: none">tenderness</div>
            </div>

            <div class="divTableCell" id="1069">
                <div class="framenr">1069</div>
                <div class="kanji">伐</div>
                <div class="keyword" style="display: none">fell</div>
            </div>

            <div class="divTableCell" id="1070">
                <div class="framenr">1070</div>
                <div class="kanji">宿</div>
                <div class="keyword" style="display: none">inn</div>
            </div>

            <div class="divTableCell" id="1071">
                <div class="framenr">1071</div>
                <div class="kanji">傷</div>
                <div class="keyword" style="display: none">wound</div>
            </div>

            <div class="divTableCell" id="1072">
                <div class="framenr">1072</div>
                <div class="kanji">保</div>
                <div class="keyword" style="display: none">protect</div>
            </div>

            <div class="divTableCell" id="1073">
                <div class="framenr">1073</div>
                <div class="kanji">褒</div>
                <div class="keyword" style="display: none">praise</div>
            </div>

            <div class="divTableCell" id="1074">
                <div class="framenr">1074</div>
                <div class="kanji">傑</div>
                <div class="keyword" style="display: none">greatness</div>
            </div>

            <div class="divTableCell" id="1075">
                <div class="framenr">1075</div>
                <div class="kanji">付</div>
                <div class="keyword" style="display: none">adhere</div>
            </div>

            <div class="divTableCell" id="1076">
                <div class="framenr">1076</div>
                <div class="kanji">符</div>
                <div class="keyword" style="display: none">token</div>
            </div>

            <div class="divTableCell" id="1077">
                <div class="framenr">1077</div>
                <div class="kanji">府</div>
                <div class="keyword" style="display: none">municipality</div>
            </div>

            <div class="divTableCell" id="1078">
                <div class="framenr">1078</div>
                <div class="kanji">任</div>
                <div class="keyword" style="display: none">responsibility</div>
            </div>

            <div class="divTableCell" id="1079">
                <div class="framenr">1079</div>
                <div class="kanji">賃</div>
                <div class="keyword" style="display: none">fare</div>
            </div>

            <div class="divTableCell" id="1080">
                <div class="framenr">1080</div>
                <div class="kanji">代</div>
                <div class="keyword" style="display: none">substitute</div>
            </div>

            <div class="divTableCell" id="1081">
                <div class="framenr">1081</div>
                <div class="kanji">袋</div>
                <div class="keyword" style="display: none">sack</div>
            </div>

            <div class="divTableCell" id="1082">
                <div class="framenr">1082</div>
                <div class="kanji">貸</div>
                <div class="keyword" style="display: none">lend</div>
            </div>

            <div class="divTableCell" id="1083">
                <div class="framenr">1083</div>
                <div class="kanji">化</div>
                <div class="keyword" style="display: none">change</div>
            </div>

            <div class="divTableCell" id="1084">
                <div class="framenr">1084</div>
                <div class="kanji">花</div>
                <div class="keyword" style="display: none">flower</div>
            </div>

            <div class="divTableCell" id="1085">
                <div class="framenr">1085</div>
                <div class="kanji">貨</div>
                <div class="keyword" style="display: none">freight</div>
            </div>

            <div class="divTableCell" id="1086">
                <div class="framenr">1086</div>
                <div class="kanji">傾</div>
                <div class="keyword" style="display: none">lean</div>
            </div>

            <div class="divTableCell" id="1087">
                <div class="framenr">1087</div>
                <div class="kanji">何</div>
                <div class="keyword" style="display: none">what</div>
            </div>

            <div class="divTableCell" id="1088">
                <div class="framenr">1088</div>
                <div class="kanji">荷</div>
                <div class="keyword" style="display: none">baggage</div>
            </div>

            <div class="divTableCell" id="1089">
                <div class="framenr">1089</div>
                <div class="kanji">俊</div>
                <div class="keyword" style="display: none">sagacious</div>
            </div>

            <div class="divTableCell" id="1090">
                <div class="framenr">1090</div>
                <div class="kanji">傍</div>
                <div class="keyword" style="display: none">bystander</div>
            </div>

            <div class="divTableCell" id="1091">
                <div class="framenr">1091</div>
                <div class="kanji">俺</div>
                <div class="keyword" style="display: none">myself</div>
            </div>

            <div class="divTableCell" id="1092">
                <div class="framenr">1092</div>
                <div class="kanji">久</div>
                <div class="keyword" style="display: none">long time</div>
            </div>

            <div class="divTableCell" id="1093">
                <div class="framenr">1093</div>
                <div class="kanji">畝</div>
                <div class="keyword" style="display: none">furrow</div>
            </div>

            <div class="divTableCell" id="1094">
                <div class="framenr">1094</div>
                <div class="kanji">囚</div>
                <div class="keyword" style="display: none">captured</div>
            </div>

            <div class="divTableCell" id="1095">
                <div class="framenr">1095</div>
                <div class="kanji">内</div>
                <div class="keyword" style="display: none">inside</div>
            </div>

            <div class="divTableCell" id="1096">
                <div class="framenr">1096</div>
                <div class="kanji">丙</div>
                <div class="keyword" style="display: none">third class</div>
            </div>

            <div class="divTableCell" id="1097">
                <div class="framenr">1097</div>
                <div class="kanji">柄</div>
                <div class="keyword" style="display: none">design</div>
            </div>

            <div class="divTableCell" id="1098">
                <div class="framenr">1098</div>
                <div class="kanji">肉</div>
                <div class="keyword" style="display: none">meat</div>
            </div>

            <div class="divTableCell" id="1099">
                <div class="framenr">1099</div>
                <div class="kanji">腐</div>
                <div class="keyword" style="display: none">rot</div>
            </div>

            <div class="divTableCell" id="1100">
                <div class="framenr">1100</div>
                <div class="kanji">座</div>
                <div class="keyword" style="display: none">sit</div>
            </div>

            <div class="divTableCell" id="1101">
                <div class="framenr">1101</div>
                <div class="kanji">挫</div>
                <div class="keyword" style="display: none">sprain</div>
            </div>

            <div class="divTableCell" id="1102">
                <div class="framenr">1102</div>
                <div class="kanji">卒</div>
                <div class="keyword" style="display: none">graduate</div>
            </div>

            <div class="divTableCell" id="1103">
                <div class="framenr">1103</div>
                <div class="kanji">傘</div>
                <div class="keyword" style="display: none">umbrella</div>
            </div>

            <div class="divTableCell" id="1104">
                <div class="framenr">1104</div>
                <div class="kanji">匁</div>
                <div class="keyword" style="display: none">monme</div>
            </div>

            <div class="divTableCell" id="1105">
                <div class="framenr">1105</div>
                <div class="kanji">以</div>
                <div class="keyword" style="display: none">by means of</div>
            </div>

            <div class="divTableCell" id="1106">
                <div class="framenr">1106</div>
                <div class="kanji">似</div>
                <div class="keyword" style="display: none">similar</div>
            </div>

            <div class="divTableCell" id="1107">
                <div class="framenr">1107</div>
                <div class="kanji">併</div>
                <div class="keyword" style="display: none">join</div>
            </div>

            <div class="divTableCell" id="1108">
                <div class="framenr">1108</div>
                <div class="kanji">瓦</div>
                <div class="keyword" style="display: none">tile</div>
            </div>

            <div class="divTableCell" id="1109">
                <div class="framenr">1109</div>
                <div class="kanji">瓶</div>
                <div class="keyword" style="display: none">flower pot</div>
            </div>

            <div class="divTableCell" id="1110">
                <div class="framenr">1110</div>
                <div class="kanji">宮</div>
                <div class="keyword" style="display: none">Shinto shrine</div>
            </div>

            <div class="divTableCell" id="1111">
                <div class="framenr">1111</div>
                <div class="kanji">営</div>
                <div class="keyword" style="display: none">occupation</div>
            </div>

            <div class="divTableCell" id="1112">
                <div class="framenr">1112</div>
                <div class="kanji">善</div>
                <div class="keyword" style="display: none">virtuous</div>
            </div>

            <div class="divTableCell" id="1113">
                <div class="framenr">1113</div>
                <div class="kanji">膳</div>
                <div class="keyword" style="display: none">dining tray</div>
            </div>

            <div class="divTableCell" id="1114">
                <div class="framenr">1114</div>
                <div class="kanji">年</div>
                <div class="keyword" style="display: none">year</div>
            </div>

            <div class="divTableCell" id="1115">
                <div class="framenr">1115</div>
                <div class="kanji">夜</div>
                <div class="keyword" style="display: none">night</div>
            </div>

            <div class="divTableCell" id="1116">
                <div class="framenr">1116</div>
                <div class="kanji">液</div>
                <div class="keyword" style="display: none">fluid</div>
            </div>

            <div class="divTableCell" id="1117">
                <div class="framenr">1117</div>
                <div class="kanji">塚</div>
                <div class="keyword" style="display: none">hillock</div>
            </div>

            <div class="divTableCell" id="1118">
                <div class="framenr">1118</div>
                <div class="kanji">幣</div>
                <div class="keyword" style="display: none">cash</div>
            </div>

            <div class="divTableCell" id="1119">
                <div class="framenr">1119</div>
                <div class="kanji">蔽</div>
                <div class="keyword" style="display: none">cover over</div>
            </div>

            <div class="divTableCell" id="1120">
                <div class="framenr">1120</div>
                <div class="kanji">弊</div>
                <div class="keyword" style="display: none">abuse</div>
            </div>

            <div class="divTableCell" id="1121">
                <div class="framenr">1121</div>
                <div class="kanji">喚</div>
                <div class="keyword" style="display: none">yell</div>
            </div>

            <div class="divTableCell" id="1122">
                <div class="framenr">1122</div>
                <div class="kanji">換</div>
                <div class="keyword" style="display: none">interchange</div>
            </div>

            <div class="divTableCell" id="1123">
                <div class="framenr">1123</div>
                <div class="kanji">融</div>
                <div class="keyword" style="display: none">dissolve</div>
            </div>

            <div class="divTableCell" id="1124">
                <div class="framenr">1124</div>
                <div class="kanji">施</div>
                <div class="keyword" style="display: none">alms</div>
            </div>

            <div class="divTableCell" id="1125">
                <div class="framenr">1125</div>
                <div class="kanji">旋</div>
                <div class="keyword" style="display: none">rotation</div>
            </div>

            <div class="divTableCell" id="1126">
                <div class="framenr">1126</div>
                <div class="kanji">遊</div>
                <div class="keyword" style="display: none">play</div>
            </div>

            <div class="divTableCell" id="1127">
                <div class="framenr">1127</div>
                <div class="kanji">旅</div>
                <div class="keyword" style="display: none">trip</div>
            </div>

            <div class="divTableCell" id="1128">
                <div class="framenr">1128</div>
                <div class="kanji">勿</div>
                <div class="keyword" style="display: none">not</div>
            </div>

            <div class="divTableCell" id="1129">
                <div class="framenr">1129</div>
                <div class="kanji">物</div>
                <div class="keyword" style="display: none">thing</div>
            </div>

            <div class="divTableCell" id="1130">
                <div class="framenr">1130</div>
                <div class="kanji">易</div>
                <div class="keyword" style="display: none">easy</div>
            </div>

            <div class="divTableCell" id="1131">
                <div class="framenr">1131</div>
                <div class="kanji">賜</div>
                <div class="keyword" style="display: none">grant</div>
            </div>

            <div class="divTableCell" id="1132">
                <div class="framenr">1132</div>
                <div class="kanji">尿</div>
                <div class="keyword" style="display: none">urine</div>
            </div>

            <div class="divTableCell" id="1133">
                <div class="framenr">1133</div>
                <div class="kanji">尼</div>
                <div class="keyword" style="display: none">nun</div>
            </div>

            <div class="divTableCell" id="1134">
                <div class="framenr">1134</div>
                <div class="kanji">尻</div>
                <div class="keyword" style="display: none">buttocks</div>
            </div>

            <div class="divTableCell" id="1135">
                <div class="framenr">1135</div>
                <div class="kanji">泥</div>
                <div class="keyword" style="display: none">mud</div>
            </div>

            <div class="divTableCell" id="1136">
                <div class="framenr">1136</div>
                <div class="kanji">塀</div>
                <div class="keyword" style="display: none">fence</div>
            </div>

            <div class="divTableCell" id="1137">
                <div class="framenr">1137</div>
                <div class="kanji">履</div>
                <div class="keyword" style="display: none">footgear</div>
            </div>

            <div class="divTableCell" id="1138">
                <div class="framenr">1138</div>
                <div class="kanji">屋</div>
                <div class="keyword" style="display: none">roof</div>
            </div>

            <div class="divTableCell" id="1139">
                <div class="framenr">1139</div>
                <div class="kanji">握</div>
                <div class="keyword" style="display: none">grip</div>
            </div>

            <div class="divTableCell" id="1140">
                <div class="framenr">1140</div>
                <div class="kanji">屈</div>
                <div class="keyword" style="display: none">yield</div>
            </div>

            <div class="divTableCell" id="1141">
                <div class="framenr">1141</div>
                <div class="kanji">掘</div>
                <div class="keyword" style="display: none">dig</div>
            </div>

            <div class="divTableCell" id="1142">
                <div class="framenr">1142</div>
                <div class="kanji">堀</div>
                <div class="keyword" style="display: none">ditch</div>
            </div>

            <div class="divTableCell" id="1143">
                <div class="framenr">1143</div>
                <div class="kanji">居</div>
                <div class="keyword" style="display: none">reside</div>
            </div>

            <div class="divTableCell" id="1144">
                <div class="framenr">1144</div>
                <div class="kanji">据</div>
                <div class="keyword" style="display: none">set</div>
            </div>

            <div class="divTableCell" id="1145">
                <div class="framenr">1145</div>
                <div class="kanji">裾</div>
                <div class="keyword" style="display: none">hem</div>
            </div>

            <div class="divTableCell" id="1146">
                <div class="framenr">1146</div>
                <div class="kanji">層</div>
                <div class="keyword" style="display: none">stratum</div>
            </div>

            <div class="divTableCell" id="1147">
                <div class="framenr">1147</div>
                <div class="kanji">局</div>
                <div class="keyword" style="display: none">bureau</div>
            </div>

            <div class="divTableCell" id="1148">
                <div class="framenr">1148</div>
                <div class="kanji">遅</div>
                <div class="keyword" style="display: none">slow</div>
            </div>

            <div class="divTableCell" id="1149">
                <div class="framenr">1149</div>
                <div class="kanji">漏</div>
                <div class="keyword" style="display: none">leak</div>
            </div>

            <div class="divTableCell" id="1150">
                <div class="framenr">1150</div>
                <div class="kanji">刷</div>
                <div class="keyword" style="display: none">printing</div>
            </div>

            <div class="divTableCell" id="1151">
                <div class="framenr">1151</div>
                <div class="kanji">尺</div>
                <div class="keyword" style="display: none">shaku</div>
            </div>

            <div class="divTableCell" id="1152">
                <div class="framenr">1152</div>
                <div class="kanji">尽</div>
                <div class="keyword" style="display: none">exhaust</div>
            </div>

            <div class="divTableCell" id="1153">
                <div class="framenr">1153</div>
                <div class="kanji">沢</div>
                <div class="keyword" style="display: none">swamp</div>
            </div>

            <div class="divTableCell" id="1154">
                <div class="framenr">1154</div>
                <div class="kanji">訳</div>
                <div class="keyword" style="display: none">translate</div>
            </div>

            <div class="divTableCell" id="1155">
                <div class="framenr">1155</div>
                <div class="kanji">択</div>
                <div class="keyword" style="display: none">choose</div>
            </div>

            <div class="divTableCell" id="1156">
                <div class="framenr">1156</div>
                <div class="kanji">昼</div>
                <div class="keyword" style="display: none">daytime</div>
            </div>

            <div class="divTableCell" id="1157">
                <div class="framenr">1157</div>
                <div class="kanji">戸</div>
                <div class="keyword" style="display: none">door</div>
            </div>

            <div class="divTableCell" id="1158">
                <div class="framenr">1158</div>
                <div class="kanji">肩</div>
                <div class="keyword" style="display: none">shoulder</div>
            </div>

            <div class="divTableCell" id="1159">
                <div class="framenr">1159</div>
                <div class="kanji">房</div>
                <div class="keyword" style="display: none">tassel</div>
            </div>

            <div class="divTableCell" id="1160">
                <div class="framenr">1160</div>
                <div class="kanji">扇</div>
                <div class="keyword" style="display: none">fan</div>
            </div>

            <div class="divTableCell" id="1161">
                <div class="framenr">1161</div>
                <div class="kanji">炉</div>
                <div class="keyword" style="display: none">hearth</div>
            </div>

            <div class="divTableCell" id="1162">
                <div class="framenr">1162</div>
                <div class="kanji">戻</div>
                <div class="keyword" style="display: none">re-</div>
            </div>

            <div class="divTableCell" id="1163">
                <div class="framenr">1163</div>
                <div class="kanji">涙</div>
                <div class="keyword" style="display: none">tears</div>
            </div>

            <div class="divTableCell" id="1164">
                <div class="framenr">1164</div>
                <div class="kanji">雇</div>
                <div class="keyword" style="display: none">employ</div>
            </div>

            <div class="divTableCell" id="1165">
                <div class="framenr">1165</div>
                <div class="kanji">顧</div>
                <div class="keyword" style="display: none">look back</div>
            </div>

            <div class="divTableCell" id="1166">
                <div class="framenr">1166</div>
                <div class="kanji">啓</div>
                <div class="keyword" style="display: none">disclose</div>
            </div>

            <div class="divTableCell" id="1167">
                <div class="framenr">1167</div>
                <div class="kanji">示</div>
                <div class="keyword" style="display: none">show</div>
            </div>

            <div class="divTableCell" id="1168">
                <div class="framenr">1168</div>
                <div class="kanji">礼</div>
                <div class="keyword" style="display: none">salutation</div>
            </div>

            <div class="divTableCell" id="1169">
                <div class="framenr">1169</div>
                <div class="kanji">祥</div>
                <div class="keyword" style="display: none">auspicious</div>
            </div>

            <div class="divTableCell" id="1170">
                <div class="framenr">1170</div>
                <div class="kanji">祝</div>
                <div class="keyword" style="display: none">celebrate</div>
            </div>

            <div class="divTableCell" id="1171">
                <div class="framenr">1171</div>
                <div class="kanji">福</div>
                <div class="keyword" style="display: none">blessing</div>
            </div>

            <div class="divTableCell" id="1172">
                <div class="framenr">1172</div>
                <div class="kanji">祉</div>
                <div class="keyword" style="display: none">welfare</div>
            </div>

            <div class="divTableCell" id="1173">
                <div class="framenr">1173</div>
                <div class="kanji">社</div>
                <div class="keyword" style="display: none">company</div>
            </div>

            <div class="divTableCell" id="1174">
                <div class="framenr">1174</div>
                <div class="kanji">視</div>
                <div class="keyword" style="display: none">inspection</div>
            </div>

            <div class="divTableCell" id="1175">
                <div class="framenr">1175</div>
                <div class="kanji">奈</div>
                <div class="keyword" style="display: none">Nara</div>
            </div>

            <div class="divTableCell" id="1176">
                <div class="framenr">1176</div>
                <div class="kanji">尉</div>
                <div class="keyword" style="display: none">military officer</div>
            </div>

            <div class="divTableCell" id="1177">
                <div class="framenr">1177</div>
                <div class="kanji">慰</div>
                <div class="keyword" style="display: none">consolation</div>
            </div>

            <div class="divTableCell" id="1178">
                <div class="framenr">1178</div>
                <div class="kanji">款</div>
                <div class="keyword" style="display: none">goodwill</div>
            </div>

            <div class="divTableCell" id="1179">
                <div class="framenr">1179</div>
                <div class="kanji">禁</div>
                <div class="keyword" style="display: none">prohibition</div>
            </div>

            <div class="divTableCell" id="1180">
                <div class="framenr">1180</div>
                <div class="kanji">襟</div>
                <div class="keyword" style="display: none">collar</div>
            </div>

            <div class="divTableCell" id="1181">
                <div class="framenr">1181</div>
                <div class="kanji">宗</div>
                <div class="keyword" style="display: none">religion</div>
            </div>

            <div class="divTableCell" id="1182">
                <div class="framenr">1182</div>
                <div class="kanji">崇</div>
                <div class="keyword" style="display: none">adore</div>
            </div>

            <div class="divTableCell" id="1183">
                <div class="framenr">1183</div>
                <div class="kanji">祭</div>
                <div class="keyword" style="display: none">ritual</div>
            </div>

            <div class="divTableCell" id="1184">
                <div class="framenr">1184</div>
                <div class="kanji">察</div>
                <div class="keyword" style="display: none">guess</div>
            </div>

            <div class="divTableCell" id="1185">
                <div class="framenr">1185</div>
                <div class="kanji">擦</div>
                <div class="keyword" style="display: none">grate</div>
            </div>

            <div class="divTableCell" id="1186">
                <div class="framenr">1186</div>
                <div class="kanji">由</div>
                <div class="keyword" style="display: none">wherefore</div>
            </div>

            <div class="divTableCell" id="1187">
                <div class="framenr">1187</div>
                <div class="kanji">抽</div>
                <div class="keyword" style="display: none">pluck</div>
            </div>

            <div class="divTableCell" id="1188">
                <div class="framenr">1188</div>
                <div class="kanji">油</div>
                <div class="keyword" style="display: none">oil</div>
            </div>

            <div class="divTableCell" id="1189">
                <div class="framenr">1189</div>
                <div class="kanji">袖</div>
                <div class="keyword" style="display: none">sleeve</div>
            </div>

            <div class="divTableCell" id="1190">
                <div class="framenr">1190</div>
                <div class="kanji">宙</div>
                <div class="keyword" style="display: none">mid-air</div>
            </div>

            <div class="divTableCell" id="1191">
                <div class="framenr">1191</div>
                <div class="kanji">届</div>
                <div class="keyword" style="display: none">deliver</div>
            </div>

            <div class="divTableCell" id="1192">
                <div class="framenr">1192</div>
                <div class="kanji">笛</div>
                <div class="keyword" style="display: none">flute</div>
            </div>

            <div class="divTableCell" id="1193">
                <div class="framenr">1193</div>
                <div class="kanji">軸</div>
                <div class="keyword" style="display: none">axis</div>
            </div>

            <div class="divTableCell" id="1194">
                <div class="framenr">1194</div>
                <div class="kanji">甲</div>
                <div class="keyword" style="display: none">armor</div>
            </div>

            <div class="divTableCell" id="1195">
                <div class="framenr">1195</div>
                <div class="kanji">押</div>
                <div class="keyword" style="display: none">push</div>
            </div>

            <div class="divTableCell" id="1196">
                <div class="framenr">1196</div>
                <div class="kanji">岬</div>
                <div class="keyword" style="display: none">headland</div>
            </div>

            <div class="divTableCell" id="1197">
                <div class="framenr">1197</div>
                <div class="kanji">挿</div>
                <div class="keyword" style="display: none">insert</div>
            </div>

            <div class="divTableCell" id="1198">
                <div class="framenr">1198</div>
                <div class="kanji">申</div>
                <div class="keyword" style="display: none">speaketh</div>
            </div>

            <div class="divTableCell" id="1199">
                <div class="framenr">1199</div>
                <div class="kanji">伸</div>
                <div class="keyword" style="display: none">expand</div>
            </div>

            <div class="divTableCell" id="1200">
                <div class="framenr">1200</div>
                <div class="kanji">神</div>
                <div class="keyword" style="display: none">gods</div>
            </div>

            <div class="divTableCell" id="1201">
                <div class="framenr">1201</div>
                <div class="kanji">捜</div>
                <div class="keyword" style="display: none">search</div>
            </div>

            <div class="divTableCell" id="1202">
                <div class="framenr">1202</div>
                <div class="kanji">果</div>
                <div class="keyword" style="display: none">fruit</div>
            </div>

            <div class="divTableCell" id="1203">
                <div class="framenr">1203</div>
                <div class="kanji">菓</div>
                <div class="keyword" style="display: none">confectionary</div>
            </div>

            <div class="divTableCell" id="1204">
                <div class="framenr">1204</div>
                <div class="kanji">課</div>
                <div class="keyword" style="display: none">chapter</div>
            </div>

            <div class="divTableCell" id="1205">
                <div class="framenr">1205</div>
                <div class="kanji">裸</div>
                <div class="keyword" style="display: none">naked</div>
            </div>

            <div class="divTableCell" id="1206">
                <div class="framenr">1206</div>
                <div class="kanji">斤</div>
                <div class="keyword" style="display: none">ax</div>
            </div>

            <div class="divTableCell" id="1207">
                <div class="framenr">1207</div>
                <div class="kanji">析</div>
                <div class="keyword" style="display: none">chop</div>
            </div>

            <div class="divTableCell" id="1208">
                <div class="framenr">1208</div>
                <div class="kanji">所</div>
                <div class="keyword" style="display: none">place</div>
            </div>

            <div class="divTableCell" id="1209">
                <div class="framenr">1209</div>
                <div class="kanji">祈</div>
                <div class="keyword" style="display: none">pray</div>
            </div>

            <div class="divTableCell" id="1210">
                <div class="framenr">1210</div>
                <div class="kanji">近</div>
                <div class="keyword" style="display: none">near</div>
            </div>

            <div class="divTableCell" id="1211">
                <div class="framenr">1211</div>
                <div class="kanji">折</div>
                <div class="keyword" style="display: none">fold</div>
            </div>

            <div class="divTableCell" id="1212">
                <div class="framenr">1212</div>
                <div class="kanji">哲</div>
                <div class="keyword" style="display: none">philosophy</div>
            </div>

            <div class="divTableCell" id="1213">
                <div class="framenr">1213</div>
                <div class="kanji">逝</div>
                <div class="keyword" style="display: none">departed</div>
            </div>

            <div class="divTableCell" id="1214">
                <div class="framenr">1214</div>
                <div class="kanji">誓</div>
                <div class="keyword" style="display: none">vow</div>
            </div>

            <div class="divTableCell" id="1215">
                <div class="framenr">1215</div>
                <div class="kanji">斬</div>
                <div class="keyword" style="display: none">chop off</div>
            </div>

            <div class="divTableCell" id="1216">
                <div class="framenr">1216</div>
                <div class="kanji">暫</div>
                <div class="keyword" style="display: none">temporarily</div>
            </div>

            <div class="divTableCell" id="1217">
                <div class="framenr">1217</div>
                <div class="kanji">漸</div>
                <div class="keyword" style="display: none">steadily</div>
            </div>

            <div class="divTableCell" id="1218">
                <div class="framenr">1218</div>
                <div class="kanji">断</div>
                <div class="keyword" style="display: none">severance</div>
            </div>

            <div class="divTableCell" id="1219">
                <div class="framenr">1219</div>
                <div class="kanji">質</div>
                <div class="keyword" style="display: none">substance</div>
            </div>

            <div class="divTableCell" id="1220">
                <div class="framenr">1220</div>
                <div class="kanji">斥</div>
                <div class="keyword" style="display: none">reject</div>
            </div>

            <div class="divTableCell" id="1221">
                <div class="framenr">1221</div>
                <div class="kanji">訴</div>
                <div class="keyword" style="display: none">accusation</div>
            </div>

            <div class="divTableCell" id="1222">
                <div class="framenr">1222</div>
                <div class="kanji">昨</div>
                <div class="keyword" style="display: none">yesterday</div>
            </div>

            <div class="divTableCell" id="1223">
                <div class="framenr">1223</div>
                <div class="kanji">詐</div>
                <div class="keyword" style="display: none">lie</div>
            </div>

            <div class="divTableCell" id="1224">
                <div class="framenr">1224</div>
                <div class="kanji">作</div>
                <div class="keyword" style="display: none">make</div>
            </div>

            <div class="divTableCell" id="1225">
                <div class="framenr">1225</div>
                <div class="kanji">雪</div>
                <div class="keyword" style="display: none">snow</div>
            </div>

            <div class="divTableCell" id="1226">
                <div class="framenr">1226</div>
                <div class="kanji">録</div>
                <div class="keyword" style="display: none">record</div>
            </div>

            <div class="divTableCell" id="1227">
                <div class="framenr">1227</div>
                <div class="kanji">剥</div>
                <div class="keyword" style="display: none">peel off</div>
            </div>

            <div class="divTableCell" id="1228">
                <div class="framenr">1228</div>
                <div class="kanji">尋</div>
                <div class="keyword" style="display: none">inquire</div>
            </div>

            <div class="divTableCell" id="1229">
                <div class="framenr">1229</div>
                <div class="kanji">急</div>
                <div class="keyword" style="display: none">hurry</div>
            </div>

            <div class="divTableCell" id="1230">
                <div class="framenr">1230</div>
                <div class="kanji">穏</div>
                <div class="keyword" style="display: none">calm</div>
            </div>

            <div class="divTableCell" id="1231">
                <div class="framenr">1231</div>
                <div class="kanji">侵</div>
                <div class="keyword" style="display: none">encroach</div>
            </div>

            <div class="divTableCell" id="1232">
                <div class="framenr">1232</div>
                <div class="kanji">浸</div>
                <div class="keyword" style="display: none">immersed</div>
            </div>

            <div class="divTableCell" id="1233">
                <div class="framenr">1233</div>
                <div class="kanji">寝</div>
                <div class="keyword" style="display: none">lie down</div>
            </div>

            <div class="divTableCell" id="1234">
                <div class="framenr">1234</div>
                <div class="kanji">婦</div>
                <div class="keyword" style="display: none">lady</div>
            </div>

            <div class="divTableCell" id="1235">
                <div class="framenr">1235</div>
                <div class="kanji">掃</div>
                <div class="keyword" style="display: none">sweep</div>
            </div>

            <div class="divTableCell" id="1236">
                <div class="framenr">1236</div>
                <div class="kanji">当</div>
                <div class="keyword" style="display: none">hit</div>
            </div>

            <div class="divTableCell" id="1237">
                <div class="framenr">1237</div>
                <div class="kanji">彙</div>
                <div class="keyword" style="display: none">glossary</div>
            </div>

            <div class="divTableCell" id="1238">
                <div class="framenr">1238</div>
                <div class="kanji">争</div>
                <div class="keyword" style="display: none">contend</div>
            </div>

            <div class="divTableCell" id="1239">
                <div class="framenr">1239</div>
                <div class="kanji">浄</div>
                <div class="keyword" style="display: none">clean</div>
            </div>

            <div class="divTableCell" id="1240">
                <div class="framenr">1240</div>
                <div class="kanji">事</div>
                <div class="keyword" style="display: none">matter</div>
            </div>

            <div class="divTableCell" id="1241">
                <div class="framenr">1241</div>
                <div class="kanji">唐</div>
                <div class="keyword" style="display: none">T'ang</div>
            </div>

            <div class="divTableCell" id="1242">
                <div class="framenr">1242</div>
                <div class="kanji">糖</div>
                <div class="keyword" style="display: none">sugar</div>
            </div>

            <div class="divTableCell" id="1243">
                <div class="framenr">1243</div>
                <div class="kanji">康</div>
                <div class="keyword" style="display: none">sane</div>
            </div>

            <div class="divTableCell" id="1244">
                <div class="framenr">1244</div>
                <div class="kanji">逮</div>
                <div class="keyword" style="display: none">apprehend</div>
            </div>

            <div class="divTableCell" id="1245">
                <div class="framenr">1245</div>
                <div class="kanji">伊</div>
                <div class="keyword" style="display: none">Italy</div>
            </div>

            <div class="divTableCell" id="1246">
                <div class="framenr">1246</div>
                <div class="kanji">君</div>
                <div class="keyword" style="display: none">old boy</div>
            </div>

            <div class="divTableCell" id="1247">
                <div class="framenr">1247</div>
                <div class="kanji">群</div>
                <div class="keyword" style="display: none">flock</div>
            </div>

            <div class="divTableCell" id="1248">
                <div class="framenr">1248</div>
                <div class="kanji">耐</div>
                <div class="keyword" style="display: none">-proof</div>
            </div>

            <div class="divTableCell" id="1249">
                <div class="framenr">1249</div>
                <div class="kanji">需</div>
                <div class="keyword" style="display: none">demand</div>
            </div>

            <div class="divTableCell" id="1250">
                <div class="framenr">1250</div>
                <div class="kanji">儒</div>
                <div class="keyword" style="display: none">Confucian</div>
            </div>

            <div class="divTableCell" id="1251">
                <div class="framenr">1251</div>
                <div class="kanji">端</div>
                <div class="keyword" style="display: none">edge</div>
            </div>

            <div class="divTableCell" id="1252">
                <div class="framenr">1252</div>
                <div class="kanji">両</div>
                <div class="keyword" style="display: none">both</div>
            </div>

            <div class="divTableCell" id="1253">
                <div class="framenr">1253</div>
                <div class="kanji">満</div>
                <div class="keyword" style="display: none">full</div>
            </div>

            <div class="divTableCell" id="1254">
                <div class="framenr">1254</div>
                <div class="kanji">画</div>
                <div class="keyword" style="display: none">brush-stroke</div>
            </div>

            <div class="divTableCell" id="1255">
                <div class="framenr">1255</div>
                <div class="kanji">歯</div>
                <div class="keyword" style="display: none">tooth</div>
            </div>

            <div class="divTableCell" id="1256">
                <div class="framenr">1256</div>
                <div class="kanji">曲</div>
                <div class="keyword" style="display: none">bend</div>
            </div>

            <div class="divTableCell" id="1257">
                <div class="framenr">1257</div>
                <div class="kanji">曹</div>
                <div class="keyword" style="display: none">cadet</div>
            </div>

            <div class="divTableCell" id="1258">
                <div class="framenr">1258</div>
                <div class="kanji">遭</div>
                <div class="keyword" style="display: none">encounter</div>
            </div>

            <div class="divTableCell" id="1259">
                <div class="framenr">1259</div>
                <div class="kanji">漕</div>
                <div class="keyword" style="display: none">rowing</div>
            </div>

            <div class="divTableCell" id="1260">
                <div class="framenr">1260</div>
                <div class="kanji">槽</div>
                <div class="keyword" style="display: none">vat</div>
            </div>

            <div class="divTableCell" id="1261">
                <div class="framenr">1261</div>
                <div class="kanji">斗</div>
                <div class="keyword" style="display: none">Big Dipper</div>
            </div>

            <div class="divTableCell" id="1262">
                <div class="framenr">1262</div>
                <div class="kanji">料</div>
                <div class="keyword" style="display: none">fee</div>
            </div>

            <div class="divTableCell" id="1263">
                <div class="framenr">1263</div>
                <div class="kanji">科</div>
                <div class="keyword" style="display: none">department</div>
            </div>

            <div class="divTableCell" id="1264">
                <div class="framenr">1264</div>
                <div class="kanji">図</div>
                <div class="keyword" style="display: none">map</div>
            </div>

            <div class="divTableCell" id="1265">
                <div class="framenr">1265</div>
                <div class="kanji">用</div>
                <div class="keyword" style="display: none">utilize</div>
            </div>

            <div class="divTableCell" id="1266">
                <div class="framenr">1266</div>
                <div class="kanji">庸</div>
                <div class="keyword" style="display: none">comfortable</div>
            </div>

            <div class="divTableCell" id="1267">
                <div class="framenr">1267</div>
                <div class="kanji">備</div>
                <div class="keyword" style="display: none">equip</div>
            </div>

            <div class="divTableCell" id="1268">
                <div class="framenr">1268</div>
                <div class="kanji">昔</div>
                <div class="keyword" style="display: none">once upon a time</div>
            </div>

            <div class="divTableCell" id="1269">
                <div class="framenr">1269</div>
                <div class="kanji">錯</div>
                <div class="keyword" style="display: none">confused</div>
            </div>

            <div class="divTableCell" id="1270">
                <div class="framenr">1270</div>
                <div class="kanji">借</div>
                <div class="keyword" style="display: none">borrow</div>
            </div>

            <div class="divTableCell" id="1271">
                <div class="framenr">1271</div>
                <div class="kanji">惜</div>
                <div class="keyword" style="display: none">pity</div>
            </div>

            <div class="divTableCell" id="1272">
                <div class="framenr">1272</div>
                <div class="kanji">措</div>
                <div class="keyword" style="display: none">set aside</div>
            </div>

            <div class="divTableCell" id="1273">
                <div class="framenr">1273</div>
                <div class="kanji">散</div>
                <div class="keyword" style="display: none">scatter</div>
            </div>

            <div class="divTableCell" id="1274">
                <div class="framenr">1274</div>
                <div class="kanji">廿</div>
                <div class="keyword" style="display: none">twenty</div>
            </div>

            <div class="divTableCell" id="1275">
                <div class="framenr">1275</div>
                <div class="kanji">庶</div>
                <div class="keyword" style="display: none">commoner</div>
            </div>

            <div class="divTableCell" id="1276">
                <div class="framenr">1276</div>
                <div class="kanji">遮</div>
                <div class="keyword" style="display: none">intercept</div>
            </div>

            <div class="divTableCell" id="1277">
                <div class="framenr">1277</div>
                <div class="kanji">席</div>
                <div class="keyword" style="display: none">seat</div>
            </div>

            <div class="divTableCell" id="1278">
                <div class="framenr">1278</div>
                <div class="kanji">度</div>
                <div class="keyword" style="display: none">degrees</div>
            </div>

            <div class="divTableCell" id="1279">
                <div class="framenr">1279</div>
                <div class="kanji">渡</div>
                <div class="keyword" style="display: none">transit</div>
            </div>

            <div class="divTableCell" id="1280">
                <div class="framenr">1280</div>
                <div class="kanji">奔</div>
                <div class="keyword" style="display: none">bustle</div>
            </div>

            <div class="divTableCell" id="1281">
                <div class="framenr">1281</div>
                <div class="kanji">噴</div>
                <div class="keyword" style="display: none">erupt</div>
            </div>

            <div class="divTableCell" id="1282">
                <div class="framenr">1282</div>
                <div class="kanji">墳</div>
                <div class="keyword" style="display: none">tomb</div>
            </div>

            <div class="divTableCell" id="1283">
                <div class="framenr">1283</div>
                <div class="kanji">憤</div>
                <div class="keyword" style="display: none">aroused</div>
            </div>

            <div class="divTableCell" id="1284">
                <div class="framenr">1284</div>
                <div class="kanji">焼</div>
                <div class="keyword" style="display: none">bake</div>
            </div>

            <div class="divTableCell" id="1285">
                <div class="framenr">1285</div>
                <div class="kanji">暁</div>
                <div class="keyword" style="display: none">daybreak</div>
            </div>

            <div class="divTableCell" id="1286">
                <div class="framenr">1286</div>
                <div class="kanji">半</div>
                <div class="keyword" style="display: none">half</div>
            </div>

            <div class="divTableCell" id="1287">
                <div class="framenr">1287</div>
                <div class="kanji">伴</div>
                <div class="keyword" style="display: none">consort</div>
            </div>

            <div class="divTableCell" id="1288">
                <div class="framenr">1288</div>
                <div class="kanji">畔</div>
                <div class="keyword" style="display: none">paddy ridge</div>
            </div>

            <div class="divTableCell" id="1289">
                <div class="framenr">1289</div>
                <div class="kanji">判</div>
                <div class="keyword" style="display: none">judgment</div>
            </div>

            <div class="divTableCell" id="1290">
                <div class="framenr">1290</div>
                <div class="kanji">拳</div>
                <div class="keyword" style="display: none">fist</div>
            </div>

            <div class="divTableCell" id="1291">
                <div class="framenr">1291</div>
                <div class="kanji">券</div>
                <div class="keyword" style="display: none">ticket</div>
            </div>

            <div class="divTableCell" id="1292">
                <div class="framenr">1292</div>
                <div class="kanji">巻</div>
                <div class="keyword" style="display: none">scroll</div>
            </div>

            <div class="divTableCell" id="1293">
                <div class="framenr">1293</div>
                <div class="kanji">圏</div>
                <div class="keyword" style="display: none">sphere</div>
            </div>

            <div class="divTableCell" id="1294">
                <div class="framenr">1294</div>
                <div class="kanji">勝</div>
                <div class="keyword" style="display: none">victory</div>
            </div>

            <div class="divTableCell" id="1295">
                <div class="framenr">1295</div>
                <div class="kanji">藤</div>
                <div class="keyword" style="display: none">wisteria</div>
            </div>

            <div class="divTableCell" id="1296">
                <div class="framenr">1296</div>
                <div class="kanji">謄</div>
                <div class="keyword" style="display: none">facsimile</div>
            </div>

            <div class="divTableCell" id="1297">
                <div class="framenr">1297</div>
                <div class="kanji">片</div>
                <div class="keyword" style="display: none">one-sided</div>
            </div>

            <div class="divTableCell" id="1298">
                <div class="framenr">1298</div>
                <div class="kanji">版</div>
                <div class="keyword" style="display: none">printing block</div>
            </div>

            <div class="divTableCell" id="1299">
                <div class="framenr">1299</div>
                <div class="kanji">之</div>
                <div class="keyword" style="display: none">of</div>
            </div>

            <div class="divTableCell" id="1300">
                <div class="framenr">1300</div>
                <div class="kanji">乏</div>
                <div class="keyword" style="display: none">destitution</div>
            </div>

            <div class="divTableCell" id="1301">
                <div class="framenr">1301</div>
                <div class="kanji">芝</div>
                <div class="keyword" style="display: none">turf</div>
            </div>

            <div class="divTableCell" id="1302">
                <div class="framenr">1302</div>
                <div class="kanji">不</div>
                <div class="keyword" style="display: none">negative</div>
            </div>

            <div class="divTableCell" id="1303">
                <div class="framenr">1303</div>
                <div class="kanji">否</div>
                <div class="keyword" style="display: none">negate</div>
            </div>

            <div class="divTableCell" id="1304">
                <div class="framenr">1304</div>
                <div class="kanji">杯</div>
                <div class="keyword" style="display: none">cupfuls</div>
            </div>

            <div class="divTableCell" id="1305">
                <div class="framenr">1305</div>
                <div class="kanji">矢</div>
                <div class="keyword" style="display: none">dart</div>
            </div>

            <div class="divTableCell" id="1306">
                <div class="framenr">1306</div>
                <div class="kanji">矯</div>
                <div class="keyword" style="display: none">rectify</div>
            </div>

            <div class="divTableCell" id="1307">
                <div class="framenr">1307</div>
                <div class="kanji">族</div>
                <div class="keyword" style="display: none">tribe</div>
            </div>

            <div class="divTableCell" id="1308">
                <div class="framenr">1308</div>
                <div class="kanji">知</div>
                <div class="keyword" style="display: none">know</div>
            </div>

            <div class="divTableCell" id="1309">
                <div class="framenr">1309</div>
                <div class="kanji">智</div>
                <div class="keyword" style="display: none">wisdom</div>
            </div>

            <div class="divTableCell" id="1310">
                <div class="framenr">1310</div>
                <div class="kanji">挨</div>
                <div class="keyword" style="display: none">shove(bar)</div>
            </div>

            <div class="divTableCell" id="1311">
                <div class="framenr">1311</div>
                <div class="kanji">矛</div>
                <div class="keyword" style="display: none">halberd</div>
            </div>

            <div class="divTableCell" id="1312">
                <div class="framenr">1312</div>
                <div class="kanji">柔</div>
                <div class="keyword" style="display: none">tender</div>
            </div>

            <div class="divTableCell" id="1313">
                <div class="framenr">1313</div>
                <div class="kanji">務</div>
                <div class="keyword" style="display: none">task</div>
            </div>

            <div class="divTableCell" id="1314">
                <div class="framenr">1314</div>
                <div class="kanji">霧</div>
                <div class="keyword" style="display: none">fog</div>
            </div>

            <div class="divTableCell" id="1315">
                <div class="framenr">1315</div>
                <div class="kanji">班</div>
                <div class="keyword" style="display: none">squad</div>
            </div>

            <div class="divTableCell" id="1316">
                <div class="framenr">1316</div>
                <div class="kanji">帰</div>
                <div class="keyword" style="display: none">homecoming</div>
            </div>

            <div class="divTableCell" id="1317">
                <div class="framenr">1317</div>
                <div class="kanji">弓</div>
                <div class="keyword" style="display: none">bow</div>
            </div>

            <div class="divTableCell" id="1318">
                <div class="framenr">1318</div>
                <div class="kanji">引</div>
                <div class="keyword" style="display: none">pull</div>
            </div>

            <div class="divTableCell" id="1319">
                <div class="framenr">1319</div>
                <div class="kanji">弔</div>
                <div class="keyword" style="display: none">condolences</div>
            </div>

            <div class="divTableCell" id="1320">
                <div class="framenr">1320</div>
                <div class="kanji">弘</div>
                <div class="keyword" style="display: none">vast</div>
            </div>

            <div class="divTableCell" id="1321">
                <div class="framenr">1321</div>
                <div class="kanji">強</div>
                <div class="keyword" style="display: none">strong</div>
            </div>

            <div class="divTableCell" id="1322">
                <div class="framenr">1322</div>
                <div class="kanji">弥</div>
                <div class="keyword" style="display: none">more and more</div>
            </div>

            <div class="divTableCell" id="1323">
                <div class="framenr">1323</div>
                <div class="kanji">弱</div>
                <div class="keyword" style="display: none">weak</div>
            </div>

            <div class="divTableCell" id="1324">
                <div class="framenr">1324</div>
                <div class="kanji">溺</div>
                <div class="keyword" style="display: none">drowning</div>
            </div>

            <div class="divTableCell" id="1325">
                <div class="framenr">1325</div>
                <div class="kanji">沸</div>
                <div class="keyword" style="display: none">seethe</div>
            </div>

            <div class="divTableCell" id="1326">
                <div class="framenr">1326</div>
                <div class="kanji">費</div>
                <div class="keyword" style="display: none">expense</div>
            </div>

            <div class="divTableCell" id="1327">
                <div class="framenr">1327</div>
                <div class="kanji">第</div>
                <div class="keyword" style="display: none">No.</div>
            </div>

            <div class="divTableCell" id="1328">
                <div class="framenr">1328</div>
                <div class="kanji">弟</div>
                <div class="keyword" style="display: none">younger brother</div>
            </div>

            <div class="divTableCell" id="1329">
                <div class="framenr">1329</div>
                <div class="kanji">巧</div>
                <div class="keyword" style="display: none">adroit</div>
            </div>

            <div class="divTableCell" id="1330">
                <div class="framenr">1330</div>
                <div class="kanji">号</div>
                <div class="keyword" style="display: none">nickname</div>
            </div>

            <div class="divTableCell" id="1331">
                <div class="framenr">1331</div>
                <div class="kanji">朽</div>
                <div class="keyword" style="display: none">decay</div>
            </div>

            <div class="divTableCell" id="1332">
                <div class="framenr">1332</div>
                <div class="kanji">誇</div>
                <div class="keyword" style="display: none">boast</div>
            </div>

            <div class="divTableCell" id="1333">
                <div class="framenr">1333</div>
                <div class="kanji">顎</div>
                <div class="keyword" style="display: none">chin</div>
            </div>

            <div class="divTableCell" id="1334">
                <div class="framenr">1334</div>
                <div class="kanji">汚</div>
                <div class="keyword" style="display: none">dirty</div>
            </div>

            <div class="divTableCell" id="1335">
                <div class="framenr">1335</div>
                <div class="kanji">与</div>
                <div class="keyword" style="display: none">bestow</div>
            </div>

            <div class="divTableCell" id="1336">
                <div class="framenr">1336</div>
                <div class="kanji">写</div>
                <div class="keyword" style="display: none">copy</div>
            </div>

            <div class="divTableCell" id="1337">
                <div class="framenr">1337</div>
                <div class="kanji">身</div>
                <div class="keyword" style="display: none">somebody</div>
            </div>

            <div class="divTableCell" id="1338">
                <div class="framenr">1338</div>
                <div class="kanji">射</div>
                <div class="keyword" style="display: none">shoot</div>
            </div>

            <div class="divTableCell" id="1339">
                <div class="framenr">1339</div>
                <div class="kanji">謝</div>
                <div class="keyword" style="display: none">apologize</div>
            </div>

            <div class="divTableCell" id="1340">
                <div class="framenr">1340</div>
                <div class="kanji">老</div>
                <div class="keyword" style="display: none">old man</div>
            </div>

            <div class="divTableCell" id="1341">
                <div class="framenr">1341</div>
                <div class="kanji">考</div>
                <div class="keyword" style="display: none">consider</div>
            </div>

            <div class="divTableCell" id="1342">
                <div class="framenr">1342</div>
                <div class="kanji">孝</div>
                <div class="keyword" style="display: none">filial piety</div>
            </div>

            <div class="divTableCell" id="1343">
                <div class="framenr">1343</div>
                <div class="kanji">教</div>
                <div class="keyword" style="display: none">teach</div>
            </div>

            <div class="divTableCell" id="1344">
                <div class="framenr">1344</div>
                <div class="kanji">拷</div>
                <div class="keyword" style="display: none">torture</div>
            </div>

            <div class="divTableCell" id="1345">
                <div class="framenr">1345</div>
                <div class="kanji">者</div>
                <div class="keyword" style="display: none">someone</div>
            </div>

            <div class="divTableCell" id="1346">
                <div class="framenr">1346</div>
                <div class="kanji">煮</div>
                <div class="keyword" style="display: none">boil</div>
            </div>

            <div class="divTableCell" id="1347">
                <div class="framenr">1347</div>
                <div class="kanji">著</div>
                <div class="keyword" style="display: none">renowned</div>
            </div>

            <div class="divTableCell" id="1348">
                <div class="framenr">1348</div>
                <div class="kanji">箸</div>
                <div class="keyword" style="display: none">chopsticks</div>
            </div>

            <div class="divTableCell" id="1349">
                <div class="framenr">1349</div>
                <div class="kanji">署</div>
                <div class="keyword" style="display: none">signature</div>
            </div>

            <div class="divTableCell" id="1350">
                <div class="framenr">1350</div>
                <div class="kanji">暑</div>
                <div class="keyword" style="display: none">sultry</div>
            </div>

            <div class="divTableCell" id="1351">
                <div class="framenr">1351</div>
                <div class="kanji">諸</div>
                <div class="keyword" style="display: none">various</div>
            </div>

            <div class="divTableCell" id="1352">
                <div class="framenr">1352</div>
                <div class="kanji">猪</div>
                <div class="keyword" style="display: none">boar</div>
            </div>

            <div class="divTableCell" id="1353">
                <div class="framenr">1353</div>
                <div class="kanji">渚</div>
                <div class="keyword" style="display: none">strand</div>
            </div>

            <div class="divTableCell" id="1354">
                <div class="framenr">1354</div>
                <div class="kanji">賭</div>
                <div class="keyword" style="display: none">gamble</div>
            </div>

            <div class="divTableCell" id="1355">
                <div class="framenr">1355</div>
                <div class="kanji">峡</div>
                <div class="keyword" style="display: none">gorge</div>
            </div>

            <div class="divTableCell" id="1356">
                <div class="framenr">1356</div>
                <div class="kanji">狭</div>
                <div class="keyword" style="display: none">cramped</div>
            </div>

            <div class="divTableCell" id="1357">
                <div class="framenr">1357</div>
                <div class="kanji">挟</div>
                <div class="keyword" style="display: none">sandwiched</div>
            </div>

            <div class="divTableCell" id="1358">
                <div class="framenr">1358</div>
                <div class="kanji">頬</div>
                <div class="keyword" style="display: none">cheek</div>
            </div>

            <div class="divTableCell" id="1359">
                <div class="framenr">1359</div>
                <div class="kanji">追</div>
                <div class="keyword" style="display: none">chase</div>
            </div>

            <div class="divTableCell" id="1360">
                <div class="framenr">1360</div>
                <div class="kanji">阜</div>
                <div class="keyword" style="display: none">large hill</div>
            </div>

            <div class="divTableCell" id="1361">
                <div class="framenr">1361</div>
                <div class="kanji">師</div>
                <div class="keyword" style="display: none">expert</div>
            </div>

            <div class="divTableCell" id="1362">
                <div class="framenr">1362</div>
                <div class="kanji">帥</div>
                <div class="keyword" style="display: none">commander</div>
            </div>

            <div class="divTableCell" id="1363">
                <div class="framenr">1363</div>
                <div class="kanji">官</div>
                <div class="keyword" style="display: none">bureaucrat</div>
            </div>

            <div class="divTableCell" id="1364">
                <div class="framenr">1364</div>
                <div class="kanji">棺</div>
                <div class="keyword" style="display: none">coffin</div>
            </div>

            <div class="divTableCell" id="1365">
                <div class="framenr">1365</div>
                <div class="kanji">管</div>
                <div class="keyword" style="display: none">pipe</div>
            </div>

            <div class="divTableCell" id="1366">
                <div class="framenr">1366</div>
                <div class="kanji">父</div>
                <div class="keyword" style="display: none">father</div>
            </div>

            <div class="divTableCell" id="1367">
                <div class="framenr">1367</div>
                <div class="kanji">釜</div>
                <div class="keyword" style="display: none">cauldron</div>
            </div>

            <div class="divTableCell" id="1368">
                <div class="framenr">1368</div>
                <div class="kanji">交</div>
                <div class="keyword" style="display: none">mingle</div>
            </div>

            <div class="divTableCell" id="1369">
                <div class="framenr">1369</div>
                <div class="kanji">効</div>
                <div class="keyword" style="display: none">merit (efficacy)</div>
            </div>

            <div class="divTableCell" id="1370">
                <div class="framenr">1370</div>
                <div class="kanji">較</div>
                <div class="keyword" style="display: none">contrast</div>
            </div>

            <div class="divTableCell" id="1371">
                <div class="framenr">1371</div>
                <div class="kanji">校</div>
                <div class="keyword" style="display: none">exam</div>
            </div>

            <div class="divTableCell" id="1372">
                <div class="framenr">1372</div>
                <div class="kanji">足</div>
                <div class="keyword" style="display: none">leg</div>
            </div>

            <div class="divTableCell" id="1373">
                <div class="framenr">1373</div>
                <div class="kanji">促</div>
                <div class="keyword" style="display: none">stimulate</div>
            </div>

            <div class="divTableCell" id="1374">
                <div class="framenr">1374</div>
                <div class="kanji">捉</div>
                <div class="keyword" style="display: none">nab</div>
            </div>

            <div class="divTableCell" id="1375">
                <div class="framenr">1375</div>
                <div class="kanji">距</div>
                <div class="keyword" style="display: none">long-distance</div>
            </div>

            <div class="divTableCell" id="1376">
                <div class="framenr">1376</div>
                <div class="kanji">路</div>
                <div class="keyword" style="display: none">path</div>
            </div>

            <div class="divTableCell" id="1377">
                <div class="framenr">1377</div>
                <div class="kanji">露</div>
                <div class="keyword" style="display: none">dew</div>
            </div>

            <div class="divTableCell" id="1378">
                <div class="framenr">1378</div>
                <div class="kanji">跳</div>
                <div class="keyword" style="display: none">hop</div>
            </div>

            <div class="divTableCell" id="1379">
                <div class="framenr">1379</div>
                <div class="kanji">躍</div>
                <div class="keyword" style="display: none">leap</div>
            </div>

            <div class="divTableCell" id="1380">
                <div class="framenr">1380</div>
                <div class="kanji">践</div>
                <div class="keyword" style="display: none">tread</div>
            </div>

            <div class="divTableCell" id="1381">
                <div class="framenr">1381</div>
                <div class="kanji">踏</div>
                <div class="keyword" style="display: none">step</div>
            </div>

            <div class="divTableCell" id="1382">
                <div class="framenr">1382</div>
                <div class="kanji">踪</div>
                <div class="keyword" style="display: none">trail</div>
            </div>

            <div class="divTableCell" id="1383">
                <div class="framenr">1383</div>
                <div class="kanji">骨</div>
                <div class="keyword" style="display: none">skeleton</div>
            </div>

            <div class="divTableCell" id="1384">
                <div class="framenr">1384</div>
                <div class="kanji">滑</div>
                <div class="keyword" style="display: none">slippery</div>
            </div>

            <div class="divTableCell" id="1385">
                <div class="framenr">1385</div>
                <div class="kanji">髄</div>
                <div class="keyword" style="display: none">marrow</div>
            </div>

            <div class="divTableCell" id="1386">
                <div class="framenr">1386</div>
                <div class="kanji">禍</div>
                <div class="keyword" style="display: none">calamity</div>
            </div>

            <div class="divTableCell" id="1387">
                <div class="framenr">1387</div>
                <div class="kanji">渦</div>
                <div class="keyword" style="display: none">whirlpool</div>
            </div>

            <div class="divTableCell" id="1388">
                <div class="framenr">1388</div>
                <div class="kanji">鍋</div>
                <div class="keyword" style="display: none">pot</div>
            </div>

            <div class="divTableCell" id="1389">
                <div class="framenr">1389</div>
                <div class="kanji">過</div>
                <div class="keyword" style="display: none">overdo</div>
            </div>

            <div class="divTableCell" id="1390">
                <div class="framenr">1390</div>
                <div class="kanji">阪</div>
                <div class="keyword" style="display: none">Heights</div>
            </div>

            <div class="divTableCell" id="1391">
                <div class="framenr">1391</div>
                <div class="kanji">阿</div>
                <div class="keyword" style="display: none">Africa</div>
            </div>

            <div class="divTableCell" id="1392">
                <div class="framenr">1392</div>
                <div class="kanji">際</div>
                <div class="keyword" style="display: none">occasion</div>
            </div>

            <div class="divTableCell" id="1393">
                <div class="framenr">1393</div>
                <div class="kanji">障</div>
                <div class="keyword" style="display: none">hinder</div>
            </div>

            <div class="divTableCell" id="1394">
                <div class="framenr">1394</div>
                <div class="kanji">隙</div>
                <div class="keyword" style="display: none">chink</div>
            </div>

            <div class="divTableCell" id="1395">
                <div class="framenr">1395</div>
                <div class="kanji">随</div>
                <div class="keyword" style="display: none">follow</div>
            </div>

            <div class="divTableCell" id="1396">
                <div class="framenr">1396</div>
                <div class="kanji">陪</div>
                <div class="keyword" style="display: none">auxiliary</div>
            </div>

            <div class="divTableCell" id="1397">
                <div class="framenr">1397</div>
                <div class="kanji">陽</div>
                <div class="keyword" style="display: none">sunshine</div>
            </div>

            <div class="divTableCell" id="1398">
                <div class="framenr">1398</div>
                <div class="kanji">陳</div>
                <div class="keyword" style="display: none">line up</div>
            </div>

            <div class="divTableCell" id="1399">
                <div class="framenr">1399</div>
                <div class="kanji">防</div>
                <div class="keyword" style="display: none">ward off</div>
            </div>

            <div class="divTableCell" id="1400">
                <div class="framenr">1400</div>
                <div class="kanji">附</div>
                <div class="keyword" style="display: none">affixed</div>
            </div>

            <div class="divTableCell" id="1401">
                <div class="framenr">1401</div>
                <div class="kanji">院</div>
                <div class="keyword" style="display: none">Inst.</div>
            </div>

            <div class="divTableCell" id="1402">
                <div class="framenr">1402</div>
                <div class="kanji">陣</div>
                <div class="keyword" style="display: none">camp</div>
            </div>

            <div class="divTableCell" id="1403">
                <div class="framenr">1403</div>
                <div class="kanji">隊</div>
                <div class="keyword" style="display: none">regiment (party)</div>
            </div>

            <div class="divTableCell" id="1404">
                <div class="framenr">1404</div>
                <div class="kanji">墜</div>
                <div class="keyword" style="display: none">crash</div>
            </div>

            <div class="divTableCell" id="1405">
                <div class="framenr">1405</div>
                <div class="kanji">降</div>
                <div class="keyword" style="display: none">descend</div>
            </div>

            <div class="divTableCell" id="1406">
                <div class="framenr">1406</div>
                <div class="kanji">階</div>
                <div class="keyword" style="display: none">story(storey)</div>
            </div>

            <div class="divTableCell" id="1407">
                <div class="framenr">1407</div>
                <div class="kanji">陛</div>
                <div class="keyword" style="display: none">highness</div>
            </div>

            <div class="divTableCell" id="1408">
                <div class="framenr">1408</div>
                <div class="kanji">隣</div>
                <div class="keyword" style="display: none">neighboring</div>
            </div>

            <div class="divTableCell" id="1409">
                <div class="framenr">1409</div>
                <div class="kanji">隔</div>
                <div class="keyword" style="display: none">isolate</div>
            </div>

            <div class="divTableCell" id="1410">
                <div class="framenr">1410</div>
                <div class="kanji">隠</div>
                <div class="keyword" style="display: none">conceal</div>
            </div>

            <div class="divTableCell" id="1411">
                <div class="framenr">1411</div>
                <div class="kanji">堕</div>
                <div class="keyword" style="display: none">degenerate</div>
            </div>

            <div class="divTableCell" id="1412">
                <div class="framenr">1412</div>
                <div class="kanji">陥</div>
                <div class="keyword" style="display: none">collapse</div>
            </div>

            <div class="divTableCell" id="1413">
                <div class="framenr">1413</div>
                <div class="kanji">穴</div>
                <div class="keyword" style="display: none">hole</div>
            </div>

            <div class="divTableCell" id="1414">
                <div class="framenr">1414</div>
                <div class="kanji">空</div>
                <div class="keyword" style="display: none">empty</div>
            </div>

            <div class="divTableCell" id="1415">
                <div class="framenr">1415</div>
                <div class="kanji">控</div>
                <div class="keyword" style="display: none">withdraw</div>
            </div>

            <div class="divTableCell" id="1416">
                <div class="framenr">1416</div>
                <div class="kanji">突</div>
                <div class="keyword" style="display: none">stab</div>
            </div>

            <div class="divTableCell" id="1417">
                <div class="framenr">1417</div>
                <div class="kanji">究</div>
                <div class="keyword" style="display: none">research</div>
            </div>

            <div class="divTableCell" id="1418">
                <div class="framenr">1418</div>
                <div class="kanji">窒</div>
                <div class="keyword" style="display: none">plug up</div>
            </div>

            <div class="divTableCell" id="1419">
                <div class="framenr">1419</div>
                <div class="kanji">窃</div>
                <div class="keyword" style="display: none">stealth</div>
            </div>

            <div class="divTableCell" id="1420">
                <div class="framenr">1420</div>
                <div class="kanji">窟</div>
                <div class="keyword" style="display: none">cavern</div>
            </div>

            <div class="divTableCell" id="1421">
                <div class="framenr">1421</div>
                <div class="kanji">窪</div>
                <div class="keyword" style="display: none">depression</div>
            </div>

            <div class="divTableCell" id="1422">
                <div class="framenr">1422</div>
                <div class="kanji">搾</div>
                <div class="keyword" style="display: none">squeeze</div>
            </div>

            <div class="divTableCell" id="1423">
                <div class="framenr">1423</div>
                <div class="kanji">窯</div>
                <div class="keyword" style="display: none">kiln</div>
            </div>

            <div class="divTableCell" id="1424">
                <div class="framenr">1424</div>
                <div class="kanji">窮</div>
                <div class="keyword" style="display: none">hard up</div>
            </div>

            <div class="divTableCell" id="1425">
                <div class="framenr">1425</div>
                <div class="kanji">探</div>
                <div class="keyword" style="display: none">grope</div>
            </div>

            <div class="divTableCell" id="1426">
                <div class="framenr">1426</div>
                <div class="kanji">深</div>
                <div class="keyword" style="display: none">deep</div>
            </div>

            <div class="divTableCell" id="1427">
                <div class="framenr">1427</div>
                <div class="kanji">丘</div>
                <div class="keyword" style="display: none">hill</div>
            </div>

            <div class="divTableCell" id="1428">
                <div class="framenr">1428</div>
                <div class="kanji">岳</div>
                <div class="keyword" style="display: none">Point</div>
            </div>

            <div class="divTableCell" id="1429">
                <div class="framenr">1429</div>
                <div class="kanji">兵</div>
                <div class="keyword" style="display: none">soldier</div>
            </div>

            <div class="divTableCell" id="1430">
                <div class="framenr">1430</div>
                <div class="kanji">浜</div>
                <div class="keyword" style="display: none">seacoast</div>
            </div>

            <div class="divTableCell" id="1431">
                <div class="framenr">1431</div>
                <div class="kanji">糸</div>
                <div class="keyword" style="display: none">thread</div>
            </div>

            <div class="divTableCell" id="1432">
                <div class="framenr">1432</div>
                <div class="kanji">織</div>
                <div class="keyword" style="display: none">weave</div>
            </div>

            <div class="divTableCell" id="1433">
                <div class="framenr">1433</div>
                <div class="kanji">繕</div>
                <div class="keyword" style="display: none">darning</div>
            </div>

            <div class="divTableCell" id="1434">
                <div class="framenr">1434</div>
                <div class="kanji">縮</div>
                <div class="keyword" style="display: none">shrink</div>
            </div>

            <div class="divTableCell" id="1435">
                <div class="framenr">1435</div>
                <div class="kanji">繁</div>
                <div class="keyword" style="display: none">luxuriant</div>
            </div>

            <div class="divTableCell" id="1436">
                <div class="framenr">1436</div>
                <div class="kanji">縦</div>
                <div class="keyword" style="display: none">vertical</div>
            </div>

            <div class="divTableCell" id="1437">
                <div class="framenr">1437</div>
                <div class="kanji">緻</div>
                <div class="keyword" style="display: none">fine</div>
            </div>

            <div class="divTableCell" id="1438">
                <div class="framenr">1438</div>
                <div class="kanji">線</div>
                <div class="keyword" style="display: none">line</div>
            </div>

            <div class="divTableCell" id="1439">
                <div class="framenr">1439</div>
                <div class="kanji">綻</div>
                <div class="keyword" style="display: none">come apart at the seams</div>
            </div>

            <div class="divTableCell" id="1440">
                <div class="framenr">1440</div>
                <div class="kanji">締</div>
                <div class="keyword" style="display: none">tighten</div>
            </div>

            <div class="divTableCell" id="1441">
                <div class="framenr">1441</div>
                <div class="kanji">維</div>
                <div class="keyword" style="display: none">fiber</div>
            </div>

            <div class="divTableCell" id="1442">
                <div class="framenr">1442</div>
                <div class="kanji">羅</div>
                <div class="keyword" style="display: none">gauze</div>
            </div>

            <div class="divTableCell" id="1443">
                <div class="framenr">1443</div>
                <div class="kanji">練</div>
                <div class="keyword" style="display: none">practice</div>
            </div>

            <div class="divTableCell" id="1444">
                <div class="framenr">1444</div>
                <div class="kanji">緒</div>
                <div class="keyword" style="display: none">thong</div>
            </div>

            <div class="divTableCell" id="1445">
                <div class="framenr">1445</div>
                <div class="kanji">続</div>
                <div class="keyword" style="display: none">continue</div>
            </div>

            <div class="divTableCell" id="1446">
                <div class="framenr">1446</div>
                <div class="kanji">絵</div>
                <div class="keyword" style="display: none">picture</div>
            </div>

            <div class="divTableCell" id="1447">
                <div class="framenr">1447</div>
                <div class="kanji">統</div>
                <div class="keyword" style="display: none">overall</div>
            </div>

            <div class="divTableCell" id="1448">
                <div class="framenr">1448</div>
                <div class="kanji">絞</div>
                <div class="keyword" style="display: none">strangle</div>
            </div>

            <div class="divTableCell" id="1449">
                <div class="framenr">1449</div>
                <div class="kanji">給</div>
                <div class="keyword" style="display: none">salary</div>
            </div>

            <div class="divTableCell" id="1450">
                <div class="framenr">1450</div>
                <div class="kanji">絡</div>
                <div class="keyword" style="display: none">entwine</div>
            </div>

            <div class="divTableCell" id="1451">
                <div class="framenr">1451</div>
                <div class="kanji">結</div>
                <div class="keyword" style="display: none">tie</div>
            </div>

            <div class="divTableCell" id="1452">
                <div class="framenr">1452</div>
                <div class="kanji">終</div>
                <div class="keyword" style="display: none">end</div>
            </div>

            <div class="divTableCell" id="1453">
                <div class="framenr">1453</div>
                <div class="kanji">級</div>
                <div class="keyword" style="display: none">class</div>
            </div>

            <div class="divTableCell" id="1454">
                <div class="framenr">1454</div>
                <div class="kanji">紀</div>
                <div class="keyword" style="display: none">chronicle</div>
            </div>

            <div class="divTableCell" id="1455">
                <div class="framenr">1455</div>
                <div class="kanji">紅</div>
                <div class="keyword" style="display: none">crimson</div>
            </div>

            <div class="divTableCell" id="1456">
                <div class="framenr">1456</div>
                <div class="kanji">納</div>
                <div class="keyword" style="display: none">settlement</div>
            </div>

            <div class="divTableCell" id="1457">
                <div class="framenr">1457</div>
                <div class="kanji">紡</div>
                <div class="keyword" style="display: none">spinning</div>
            </div>

            <div class="divTableCell" id="1458">
                <div class="framenr">1458</div>
                <div class="kanji">紛</div>
                <div class="keyword" style="display: none">distract</div>
            </div>

            <div class="divTableCell" id="1459">
                <div class="framenr">1459</div>
                <div class="kanji">紹</div>
                <div class="keyword" style="display: none">introduce</div>
            </div>

            <div class="divTableCell" id="1460">
                <div class="framenr">1460</div>
                <div class="kanji">経</div>
                <div class="keyword" style="display: none">sutra</div>
            </div>

            <div class="divTableCell" id="1461">
                <div class="framenr">1461</div>
                <div class="kanji">紳</div>
                <div class="keyword" style="display: none">sire</div>
            </div>

            <div class="divTableCell" id="1462">
                <div class="framenr">1462</div>
                <div class="kanji">約</div>
                <div class="keyword" style="display: none">promise</div>
            </div>

            <div class="divTableCell" id="1463">
                <div class="framenr">1463</div>
                <div class="kanji">細</div>
                <div class="keyword" style="display: none">dainty</div>
            </div>

            <div class="divTableCell" id="1464">
                <div class="framenr">1464</div>
                <div class="kanji">累</div>
                <div class="keyword" style="display: none">accumulate</div>
            </div>

            <div class="divTableCell" id="1465">
                <div class="framenr">1465</div>
                <div class="kanji">索</div>
                <div class="keyword" style="display: none">cord</div>
            </div>

            <div class="divTableCell" id="1466">
                <div class="framenr">1466</div>
                <div class="kanji">総</div>
                <div class="keyword" style="display: none">general</div>
            </div>

            <div class="divTableCell" id="1467">
                <div class="framenr">1467</div>
                <div class="kanji">綿</div>
                <div class="keyword" style="display: none">cotton</div>
            </div>

            <div class="divTableCell" id="1468">
                <div class="framenr">1468</div>
                <div class="kanji">絹</div>
                <div class="keyword" style="display: none">silk</div>
            </div>

            <div class="divTableCell" id="1469">
                <div class="framenr">1469</div>
                <div class="kanji">繰</div>
                <div class="keyword" style="display: none">winding</div>
            </div>

            <div class="divTableCell" id="1470">
                <div class="framenr">1470</div>
                <div class="kanji">継</div>
                <div class="keyword" style="display: none">inherit</div>
            </div>

            <div class="divTableCell" id="1471">
                <div class="framenr">1471</div>
                <div class="kanji">緑</div>
                <div class="keyword" style="display: none">green</div>
            </div>

            <div class="divTableCell" id="1472">
                <div class="framenr">1472</div>
                <div class="kanji">縁</div>
                <div class="keyword" style="display: none">affinity</div>
            </div>

            <div class="divTableCell" id="1473">
                <div class="framenr">1473</div>
                <div class="kanji">網</div>
                <div class="keyword" style="display: none">netting</div>
            </div>

            <div class="divTableCell" id="1474">
                <div class="framenr">1474</div>
                <div class="kanji">緊</div>
                <div class="keyword" style="display: none">tense</div>
            </div>

            <div class="divTableCell" id="1475">
                <div class="framenr">1475</div>
                <div class="kanji">紫</div>
                <div class="keyword" style="display: none">purple</div>
            </div>

            <div class="divTableCell" id="1476">
                <div class="framenr">1476</div>
                <div class="kanji">縛</div>
                <div class="keyword" style="display: none">truss</div>
            </div>

            <div class="divTableCell" id="1477">
                <div class="framenr">1477</div>
                <div class="kanji">縄</div>
                <div class="keyword" style="display: none">straw rope</div>
            </div>

            <div class="divTableCell" id="1478">
                <div class="framenr">1478</div>
                <div class="kanji">幼</div>
                <div class="keyword" style="display: none">infancy</div>
            </div>

            <div class="divTableCell" id="1479">
                <div class="framenr">1479</div>
                <div class="kanji">後</div>
                <div class="keyword" style="display: none">behind</div>
            </div>

            <div class="divTableCell" id="1480">
                <div class="framenr">1480</div>
                <div class="kanji">幽</div>
                <div class="keyword" style="display: none">faint</div>
            </div>

            <div class="divTableCell" id="1481">
                <div class="framenr">1481</div>
                <div class="kanji">幾</div>
                <div class="keyword" style="display: none">how many</div>
            </div>

            <div class="divTableCell" id="1482">
                <div class="framenr">1482</div>
                <div class="kanji">機</div>
                <div class="keyword" style="display: none">mechanism</div>
            </div>

            <div class="divTableCell" id="1483">
                <div class="framenr">1483</div>
                <div class="kanji">畿</div>
                <div class="keyword" style="display: none">capital suburbs</div>
            </div>

            <div class="divTableCell" id="1484">
                <div class="framenr">1484</div>
                <div class="kanji">玄</div>
                <div class="keyword" style="display: none">mysterious</div>
            </div>

            <div class="divTableCell" id="1485">
                <div class="framenr">1485</div>
                <div class="kanji">畜</div>
                <div class="keyword" style="display: none">livestock</div>
            </div>

            <div class="divTableCell" id="1486">
                <div class="framenr">1486</div>
                <div class="kanji">蓄</div>
                <div class="keyword" style="display: none">amass</div>
            </div>

            <div class="divTableCell" id="1487">
                <div class="framenr">1487</div>
                <div class="kanji">弦</div>
                <div class="keyword" style="display: none">bowstring</div>
            </div>

            <div class="divTableCell" id="1488">
                <div class="framenr">1488</div>
                <div class="kanji">擁</div>
                <div class="keyword" style="display: none">hug</div>
            </div>

            <div class="divTableCell" id="1489">
                <div class="framenr">1489</div>
                <div class="kanji">滋</div>
                <div class="keyword" style="display: none">nourishing</div>
            </div>

            <div class="divTableCell" id="1490">
                <div class="framenr">1490</div>
                <div class="kanji">慈</div>
                <div class="keyword" style="display: none">mercy</div>
            </div>

            <div class="divTableCell" id="1491">
                <div class="framenr">1491</div>
                <div class="kanji">磁</div>
                <div class="keyword" style="display: none">magnet</div>
            </div>

            <div class="divTableCell" id="1492">
                <div class="framenr">1492</div>
                <div class="kanji">系</div>
                <div class="keyword" style="display: none">lineage</div>
            </div>

            <div class="divTableCell" id="1493">
                <div class="framenr">1493</div>
                <div class="kanji">係</div>
                <div class="keyword" style="display: none">person in charge</div>
            </div>

            <div class="divTableCell" id="1494">
                <div class="framenr">1494</div>
                <div class="kanji">孫</div>
                <div class="keyword" style="display: none">grandchild</div>
            </div>

            <div class="divTableCell" id="1495">
                <div class="framenr">1495</div>
                <div class="kanji">懸</div>
                <div class="keyword" style="display: none">suspend</div>
            </div>

            <div class="divTableCell" id="1496">
                <div class="framenr">1496</div>
                <div class="kanji">遜</div>
                <div class="keyword" style="display: none">modest</div>
            </div>

            <div class="divTableCell" id="1497">
                <div class="framenr">1497</div>
                <div class="kanji">却</div>
                <div class="keyword" style="display: none">instead</div>
            </div>

            <div class="divTableCell" id="1498">
                <div class="framenr">1498</div>
                <div class="kanji">脚</div>
                <div class="keyword" style="display: none">shins</div>
            </div>

            <div class="divTableCell" id="1499">
                <div class="framenr">1499</div>
                <div class="kanji">卸</div>
                <div class="keyword" style="display: none">wholesale</div>
            </div>

            <div class="divTableCell" id="1500">
                <div class="framenr">1500</div>
                <div class="kanji">御</div>
                <div class="keyword" style="display: none">honorable</div>
            </div>

            <div class="divTableCell" id="1501">
                <div class="framenr">1501</div>
                <div class="kanji">服</div>
                <div class="keyword" style="display: none">clothing</div>
            </div>

            <div class="divTableCell" id="1502">
                <div class="framenr">1502</div>
                <div class="kanji">命</div>
                <div class="keyword" style="display: none">fate</div>
            </div>

            <div class="divTableCell" id="1503">
                <div class="framenr">1503</div>
                <div class="kanji">令</div>
                <div class="keyword" style="display: none">orders</div>
            </div>

            <div class="divTableCell" id="1504">
                <div class="framenr">1504</div>
                <div class="kanji">零</div>
                <div class="keyword" style="display: none">zero</div>
            </div>

            <div class="divTableCell" id="1505">
                <div class="framenr">1505</div>
                <div class="kanji">齢</div>
                <div class="keyword" style="display: none">age</div>
            </div>

            <div class="divTableCell" id="1506">
                <div class="framenr">1506</div>
                <div class="kanji">冷</div>
                <div class="keyword" style="display: none">cool</div>
            </div>

            <div class="divTableCell" id="1507">
                <div class="framenr">1507</div>
                <div class="kanji">領</div>
                <div class="keyword" style="display: none">jurisdiction</div>
            </div>

            <div class="divTableCell" id="1508">
                <div class="framenr">1508</div>
                <div class="kanji">鈴</div>
                <div class="keyword" style="display: none">small bell</div>
            </div>

            <div class="divTableCell" id="1509">
                <div class="framenr">1509</div>
                <div class="kanji">勇</div>
                <div class="keyword" style="display: none">courage</div>
            </div>

            <div class="divTableCell" id="1510">
                <div class="framenr">1510</div>
                <div class="kanji">湧</div>
                <div class="keyword" style="display: none">bubble up</div>
            </div>

            <div class="divTableCell" id="1511">
                <div class="framenr">1511</div>
                <div class="kanji">通</div>
                <div class="keyword" style="display: none">traffic</div>
            </div>

            <div class="divTableCell" id="1512">
                <div class="framenr">1512</div>
                <div class="kanji">踊</div>
                <div class="keyword" style="display: none">jump</div>
            </div>

            <div class="divTableCell" id="1513">
                <div class="framenr">1513</div>
                <div class="kanji">疑</div>
                <div class="keyword" style="display: none">doubt</div>
            </div>

            <div class="divTableCell" id="1514">
                <div class="framenr">1514</div>
                <div class="kanji">擬</div>
                <div class="keyword" style="display: none">mimic</div>
            </div>

            <div class="divTableCell" id="1515">
                <div class="framenr">1515</div>
                <div class="kanji">凝</div>
                <div class="keyword" style="display: none">congeal</div>
            </div>

            <div class="divTableCell" id="1516">
                <div class="framenr">1516</div>
                <div class="kanji">範</div>
                <div class="keyword" style="display: none">pattern</div>
            </div>

            <div class="divTableCell" id="1517">
                <div class="framenr">1517</div>
                <div class="kanji">犯</div>
                <div class="keyword" style="display: none">crime</div>
            </div>

            <div class="divTableCell" id="1518">
                <div class="framenr">1518</div>
                <div class="kanji">氾</div>
                <div class="keyword" style="display: none">widespread</div>
            </div>

            <div class="divTableCell" id="1519">
                <div class="framenr">1519</div>
                <div class="kanji">厄</div>
                <div class="keyword" style="display: none">unlucky</div>
            </div>

            <div class="divTableCell" id="1520">
                <div class="framenr">1520</div>
                <div class="kanji">危</div>
                <div class="keyword" style="display: none">dangerous</div>
            </div>

            <div class="divTableCell" id="1521">
                <div class="framenr">1521</div>
                <div class="kanji">宛</div>
                <div class="keyword" style="display: none">address</div>
            </div>

            <div class="divTableCell" id="1522">
                <div class="framenr">1522</div>
                <div class="kanji">腕</div>
                <div class="keyword" style="display: none">arm</div>
            </div>

            <div class="divTableCell" id="1523">
                <div class="framenr">1523</div>
                <div class="kanji">苑</div>
                <div class="keyword" style="display: none">garden</div>
            </div>

            <div class="divTableCell" id="1524">
                <div class="framenr">1524</div>
                <div class="kanji">怨</div>
                <div class="keyword" style="display: none">grudge</div>
            </div>

            <div class="divTableCell" id="1525">
                <div class="framenr">1525</div>
                <div class="kanji">柳</div>
                <div class="keyword" style="display: none">willow</div>
            </div>

            <div class="divTableCell" id="1526">
                <div class="framenr">1526</div>
                <div class="kanji">卵</div>
                <div class="keyword" style="display: none">egg</div>
            </div>

            <div class="divTableCell" id="1527">
                <div class="framenr">1527</div>
                <div class="kanji">留</div>
                <div class="keyword" style="display: none">detain</div>
            </div>

            <div class="divTableCell" id="1528">
                <div class="framenr">1528</div>
                <div class="kanji">瑠</div>
                <div class="keyword" style="display: none">marine blue(lapislazuli)</div>
            </div>

            <div class="divTableCell" id="1529">
                <div class="framenr">1529</div>
                <div class="kanji">貿</div>
                <div class="keyword" style="display: none">trade</div>
            </div>

            <div class="divTableCell" id="1530">
                <div class="framenr">1530</div>
                <div class="kanji">印</div>
                <div class="keyword" style="display: none">stamp</div>
            </div>

            <div class="divTableCell" id="1531">
                <div class="framenr">1531</div>
                <div class="kanji">臼</div>
                <div class="keyword" style="display: none">mortar</div>
            </div>

            <div class="divTableCell" id="1532">
                <div class="framenr">1532</div>
                <div class="kanji">毀</div>
                <div class="keyword" style="display: none">break</div>
            </div>

            <div class="divTableCell" id="1533">
                <div class="framenr">1533</div>
                <div class="kanji">興</div>
                <div class="keyword" style="display: none">entertain</div>
            </div>

            <div class="divTableCell" id="1534">
                <div class="framenr">1534</div>
                <div class="kanji">酉</div>
                <div class="keyword" style="display: none">sign of the bird</div>
            </div>

            <div class="divTableCell" id="1535">
                <div class="framenr">1535</div>
                <div class="kanji">酒</div>
                <div class="keyword" style="display: none">sake</div>
            </div>

            <div class="divTableCell" id="1536">
                <div class="framenr">1536</div>
                <div class="kanji">酌</div>
                <div class="keyword" style="display: none">bartending</div>
            </div>

            <div class="divTableCell" id="1537">
                <div class="framenr">1537</div>
                <div class="kanji">酎</div>
                <div class="keyword" style="display: none">hooch</div>
            </div>

            <div class="divTableCell" id="1538">
                <div class="framenr">1538</div>
                <div class="kanji">酵</div>
                <div class="keyword" style="display: none">fermentation</div>
            </div>

            <div class="divTableCell" id="1539">
                <div class="framenr">1539</div>
                <div class="kanji">酷</div>
                <div class="keyword" style="display: none">cruel</div>
            </div>

            <div class="divTableCell" id="1540">
                <div class="framenr">1540</div>
                <div class="kanji">酬</div>
                <div class="keyword" style="display: none">repay</div>
            </div>

            <div class="divTableCell" id="1541">
                <div class="framenr">1541</div>
                <div class="kanji">酪</div>
                <div class="keyword" style="display: none">dairy products</div>
            </div>

            <div class="divTableCell" id="1542">
                <div class="framenr">1542</div>
                <div class="kanji">酢</div>
                <div class="keyword" style="display: none">vinegar</div>
            </div>

            <div class="divTableCell" id="1543">
                <div class="framenr">1543</div>
                <div class="kanji">酔</div>
                <div class="keyword" style="display: none">drunk</div>
            </div>

            <div class="divTableCell" id="1544">
                <div class="framenr">1544</div>
                <div class="kanji">配</div>
                <div class="keyword" style="display: none">distribute</div>
            </div>

            <div class="divTableCell" id="1545">
                <div class="framenr">1545</div>
                <div class="kanji">酸</div>
                <div class="keyword" style="display: none">acid</div>
            </div>

            <div class="divTableCell" id="1546">
                <div class="framenr">1546</div>
                <div class="kanji">猶</div>
                <div class="keyword" style="display: none">waver</div>
            </div>

            <div class="divTableCell" id="1547">
                <div class="framenr">1547</div>
                <div class="kanji">尊</div>
                <div class="keyword" style="display: none">revered</div>
            </div>

            <div class="divTableCell" id="1548">
                <div class="framenr">1548</div>
                <div class="kanji">豆</div>
                <div class="keyword" style="display: none">beans</div>
            </div>

            <div class="divTableCell" id="1549">
                <div class="framenr">1549</div>
                <div class="kanji">頭</div>
                <div class="keyword" style="display: none">head</div>
            </div>

            <div class="divTableCell" id="1550">
                <div class="framenr">1550</div>
                <div class="kanji">短</div>
                <div class="keyword" style="display: none">short</div>
            </div>

            <div class="divTableCell" id="1551">
                <div class="framenr">1551</div>
                <div class="kanji">豊</div>
                <div class="keyword" style="display: none">bountiful</div>
            </div>

            <div class="divTableCell" id="1552">
                <div class="framenr">1552</div>
                <div class="kanji">鼓</div>
                <div class="keyword" style="display: none">drum</div>
            </div>

            <div class="divTableCell" id="1553">
                <div class="framenr">1553</div>
                <div class="kanji">喜</div>
                <div class="keyword" style="display: none">rejoice</div>
            </div>

            <div class="divTableCell" id="1554">
                <div class="framenr">1554</div>
                <div class="kanji">樹</div>
                <div class="keyword" style="display: none">timber-trees</div>
            </div>

            <div class="divTableCell" id="1555">
                <div class="framenr">1555</div>
                <div class="kanji">皿</div>
                <div class="keyword" style="display: none">dish</div>
            </div>

            <div class="divTableCell" id="1556">
                <div class="framenr">1556</div>
                <div class="kanji">血</div>
                <div class="keyword" style="display: none">blood</div>
            </div>

            <div class="divTableCell" id="1557">
                <div class="framenr">1557</div>
                <div class="kanji">盆</div>
                <div class="keyword" style="display: none">basin</div>
            </div>

            <div class="divTableCell" id="1558">
                <div class="framenr">1558</div>
                <div class="kanji">盟</div>
                <div class="keyword" style="display: none">alliance</div>
            </div>

            <div class="divTableCell" id="1559">
                <div class="framenr">1559</div>
                <div class="kanji">盗</div>
                <div class="keyword" style="display: none">steal</div>
            </div>

            <div class="divTableCell" id="1560">
                <div class="framenr">1560</div>
                <div class="kanji">温</div>
                <div class="keyword" style="display: none">warm</div>
            </div>

            <div class="divTableCell" id="1561">
                <div class="framenr">1561</div>
                <div class="kanji">蓋</div>
                <div class="keyword" style="display: none">lid</div>
            </div>

            <div class="divTableCell" id="1562">
                <div class="framenr">1562</div>
                <div class="kanji">監</div>
                <div class="keyword" style="display: none">oversee</div>
            </div>

            <div class="divTableCell" id="1563">
                <div class="framenr">1563</div>
                <div class="kanji">濫</div>
                <div class="keyword" style="display: none">overflow</div>
            </div>

            <div class="divTableCell" id="1564">
                <div class="framenr">1564</div>
                <div class="kanji">鑑</div>
                <div class="keyword" style="display: none">specimen</div>
            </div>

            <div class="divTableCell" id="1565">
                <div class="framenr">1565</div>
                <div class="kanji">藍</div>
                <div class="keyword" style="display: none">indigo</div>
            </div>

            <div class="divTableCell" id="1566">
                <div class="framenr">1566</div>
                <div class="kanji">猛</div>
                <div class="keyword" style="display: none">fierce</div>
            </div>

            <div class="divTableCell" id="1567">
                <div class="framenr">1567</div>
                <div class="kanji">盛</div>
                <div class="keyword" style="display: none">boom</div>
            </div>

            <div class="divTableCell" id="1568">
                <div class="framenr">1568</div>
                <div class="kanji">塩</div>
                <div class="keyword" style="display: none">salt</div>
            </div>

            <div class="divTableCell" id="1569">
                <div class="framenr">1569</div>
                <div class="kanji">銀</div>
                <div class="keyword" style="display: none">silver</div>
            </div>

            <div class="divTableCell" id="1570">
                <div class="framenr">1570</div>
                <div class="kanji">恨</div>
                <div class="keyword" style="display: none">resentment</div>
            </div>

            <div class="divTableCell" id="1571">
                <div class="framenr">1571</div>
                <div class="kanji">根</div>
                <div class="keyword" style="display: none">root</div>
            </div>

            <div class="divTableCell" id="1572">
                <div class="framenr">1572</div>
                <div class="kanji">即</div>
                <div class="keyword" style="display: none">instant</div>
            </div>

            <div class="divTableCell" id="1573">
                <div class="framenr">1573</div>
                <div class="kanji">爵</div>
                <div class="keyword" style="display: none">baron</div>
            </div>

            <div class="divTableCell" id="1574">
                <div class="framenr">1574</div>
                <div class="kanji">節</div>
                <div class="keyword" style="display: none">node</div>
            </div>

            <div class="divTableCell" id="1575">
                <div class="framenr">1575</div>
                <div class="kanji">退</div>
                <div class="keyword" style="display: none">retreat</div>
            </div>

            <div class="divTableCell" id="1576">
                <div class="framenr">1576</div>
                <div class="kanji">限</div>
                <div class="keyword" style="display: none">limit</div>
            </div>

            <div class="divTableCell" id="1577">
                <div class="framenr">1577</div>
                <div class="kanji">眼</div>
                <div class="keyword" style="display: none">eyeball</div>
            </div>

            <div class="divTableCell" id="1578">
                <div class="framenr">1578</div>
                <div class="kanji">良</div>
                <div class="keyword" style="display: none">good</div>
            </div>

            <div class="divTableCell" id="1579">
                <div class="framenr">1579</div>
                <div class="kanji">朗</div>
                <div class="keyword" style="display: none">melodious</div>
            </div>

            <div class="divTableCell" id="1580">
                <div class="framenr">1580</div>
                <div class="kanji">浪</div>
                <div class="keyword" style="display: none">wandering</div>
            </div>

            <div class="divTableCell" id="1581">
                <div class="framenr">1581</div>
                <div class="kanji">娘</div>
                <div class="keyword" style="display: none">daughter</div>
            </div>

            <div class="divTableCell" id="1582">
                <div class="framenr">1582</div>
                <div class="kanji">食</div>
                <div class="keyword" style="display: none">eat</div>
            </div>

            <div class="divTableCell" id="1583">
                <div class="framenr">1583</div>
                <div class="kanji">飯</div>
                <div class="keyword" style="display: none">meal</div>
            </div>

            <div class="divTableCell" id="1584">
                <div class="framenr">1584</div>
                <div class="kanji">飲</div>
                <div class="keyword" style="display: none">drink</div>
            </div>

            <div class="divTableCell" id="1585">
                <div class="framenr">1585</div>
                <div class="kanji">飢</div>
                <div class="keyword" style="display: none">hungry</div>
            </div>

            <div class="divTableCell" id="1586">
                <div class="framenr">1586</div>
                <div class="kanji">餓</div>
                <div class="keyword" style="display: none">starve</div>
            </div>

            <div class="divTableCell" id="1587">
                <div class="framenr">1587</div>
                <div class="kanji">飾</div>
                <div class="keyword" style="display: none">decorate</div>
            </div>

            <div class="divTableCell" id="1588">
                <div class="framenr">1588</div>
                <div class="kanji">餌</div>
                <div class="keyword" style="display: none">feed</div>
            </div>

            <div class="divTableCell" id="1589">
                <div class="framenr">1589</div>
                <div class="kanji">館</div>
                <div class="keyword" style="display: none">Bldg.</div>
            </div>

            <div class="divTableCell" id="1590">
                <div class="framenr">1590</div>
                <div class="kanji">餅</div>
                <div class="keyword" style="display: none">mochi</div>
            </div>

            <div class="divTableCell" id="1591">
                <div class="framenr">1591</div>
                <div class="kanji">養</div>
                <div class="keyword" style="display: none">foster</div>
            </div>

            <div class="divTableCell" id="1592">
                <div class="framenr">1592</div>
                <div class="kanji">飽</div>
                <div class="keyword" style="display: none">sated</div>
            </div>

            <div class="divTableCell" id="1593">
                <div class="framenr">1593</div>
                <div class="kanji">既</div>
                <div class="keyword" style="display: none">previously</div>
            </div>

            <div class="divTableCell" id="1594">
                <div class="framenr">1594</div>
                <div class="kanji">概</div>
                <div class="keyword" style="display: none">outline</div>
            </div>

            <div class="divTableCell" id="1595">
                <div class="framenr">1595</div>
                <div class="kanji">慨</div>
                <div class="keyword" style="display: none">rue</div>
            </div>

            <div class="divTableCell" id="1596">
                <div class="framenr">1596</div>
                <div class="kanji">平</div>
                <div class="keyword" style="display: none">even</div>
            </div>

            <div class="divTableCell" id="1597">
                <div class="framenr">1597</div>
                <div class="kanji">呼</div>
                <div class="keyword" style="display: none">call</div>
            </div>

            <div class="divTableCell" id="1598">
                <div class="framenr">1598</div>
                <div class="kanji">坪</div>
                <div class="keyword" style="display: none">two-mat area</div>
            </div>

            <div class="divTableCell" id="1599">
                <div class="framenr">1599</div>
                <div class="kanji">評</div>
                <div class="keyword" style="display: none">evaluate</div>
            </div>

            <div class="divTableCell" id="1600">
                <div class="framenr">1600</div>
                <div class="kanji">刈</div>
                <div class="keyword" style="display: none">reap</div>
            </div>

            <div class="divTableCell" id="1601">
                <div class="framenr">1601</div>
                <div class="kanji">刹</div>
                <div class="keyword" style="display: none">moment(temple)</div>
            </div>

            <div class="divTableCell" id="1602">
                <div class="framenr">1602</div>
                <div class="kanji">希</div>
                <div class="keyword" style="display: none">hope</div>
            </div>

            <div class="divTableCell" id="1603">
                <div class="framenr">1603</div>
                <div class="kanji">凶</div>
                <div class="keyword" style="display: none">villain</div>
            </div>

            <div class="divTableCell" id="1604">
                <div class="framenr">1604</div>
                <div class="kanji">胸</div>
                <div class="keyword" style="display: none">bosom</div>
            </div>

            <div class="divTableCell" id="1605">
                <div class="framenr">1605</div>
                <div class="kanji">離</div>
                <div class="keyword" style="display: none">detach</div>
            </div>

            <div class="divTableCell" id="1606">
                <div class="framenr">1606</div>
                <div class="kanji">璃</div>
                <div class="keyword" style="display: none">crystal</div>
            </div>

            <div class="divTableCell" id="1607">
                <div class="framenr">1607</div>
                <div class="kanji">殺</div>
                <div class="keyword" style="display: none">kill</div>
            </div>

            <div class="divTableCell" id="1608">
                <div class="framenr">1608</div>
                <div class="kanji">爽</div>
                <div class="keyword" style="display: none">bracing</div>
            </div>

            <div class="divTableCell" id="1609">
                <div class="framenr">1609</div>
                <div class="kanji">純</div>
                <div class="keyword" style="display: none">genuine</div>
            </div>

            <div class="divTableCell" id="1610">
                <div class="framenr">1610</div>
                <div class="kanji">頓</div>
                <div class="keyword" style="display: none">immediate</div>
            </div>

            <div class="divTableCell" id="1611">
                <div class="framenr">1611</div>
                <div class="kanji">鈍</div>
                <div class="keyword" style="display: none">dull</div>
            </div>

            <div class="divTableCell" id="1612">
                <div class="framenr">1612</div>
                <div class="kanji">辛</div>
                <div class="keyword" style="display: none">spicy</div>
            </div>

            <div class="divTableCell" id="1613">
                <div class="framenr">1613</div>
                <div class="kanji">辞</div>
                <div class="keyword" style="display: none">resign</div>
            </div>

            <div class="divTableCell" id="1614">
                <div class="framenr">1614</div>
                <div class="kanji">梓</div>
                <div class="keyword" style="display: none">catalpa</div>
            </div>

            <div class="divTableCell" id="1615">
                <div class="framenr">1615</div>
                <div class="kanji">宰</div>
                <div class="keyword" style="display: none">superintend</div>
            </div>

            <div class="divTableCell" id="1616">
                <div class="framenr">1616</div>
                <div class="kanji">壁</div>
                <div class="keyword" style="display: none">wall</div>
            </div>

            <div class="divTableCell" id="1617">
                <div class="framenr">1617</div>
                <div class="kanji">璧</div>
                <div class="keyword" style="display: none">holed gem</div>
            </div>

            <div class="divTableCell" id="1618">
                <div class="framenr">1618</div>
                <div class="kanji">避</div>
                <div class="keyword" style="display: none">evade</div>
            </div>

            <div class="divTableCell" id="1619">
                <div class="framenr">1619</div>
                <div class="kanji">新</div>
                <div class="keyword" style="display: none">new</div>
            </div>

            <div class="divTableCell" id="1620">
                <div class="framenr">1620</div>
                <div class="kanji">薪</div>
                <div class="keyword" style="display: none">firewood</div>
            </div>

            <div class="divTableCell" id="1621">
                <div class="framenr">1621</div>
                <div class="kanji">親</div>
                <div class="keyword" style="display: none">parent</div>
            </div>

            <div class="divTableCell" id="1622">
                <div class="framenr">1622</div>
                <div class="kanji">幸</div>
                <div class="keyword" style="display: none">happiness</div>
            </div>

            <div class="divTableCell" id="1623">
                <div class="framenr">1623</div>
                <div class="kanji">執</div>
                <div class="keyword" style="display: none">tenacious</div>
            </div>

            <div class="divTableCell" id="1624">
                <div class="framenr">1624</div>
                <div class="kanji">摯</div>
                <div class="keyword" style="display: none">clasp</div>
            </div>

            <div class="divTableCell" id="1625">
                <div class="framenr">1625</div>
                <div class="kanji">報</div>
                <div class="keyword" style="display: none">report</div>
            </div>

            <div class="divTableCell" id="1626">
                <div class="framenr">1626</div>
                <div class="kanji">叫</div>
                <div class="keyword" style="display: none">shout</div>
            </div>

            <div class="divTableCell" id="1627">
                <div class="framenr">1627</div>
                <div class="kanji">糾</div>
                <div class="keyword" style="display: none">twist</div>
            </div>

            <div class="divTableCell" id="1628">
                <div class="framenr">1628</div>
                <div class="kanji">収</div>
                <div class="keyword" style="display: none">income</div>
            </div>

            <div class="divTableCell" id="1629">
                <div class="framenr">1629</div>
                <div class="kanji">卑</div>
                <div class="keyword" style="display: none">lowly</div>
            </div>

            <div class="divTableCell" id="1630">
                <div class="framenr">1630</div>
                <div class="kanji">碑</div>
                <div class="keyword" style="display: none">tombstone</div>
            </div>

            <div class="divTableCell" id="1631">
                <div class="framenr">1631</div>
                <div class="kanji">陸</div>
                <div class="keyword" style="display: none">land</div>
            </div>

            <div class="divTableCell" id="1632">
                <div class="framenr">1632</div>
                <div class="kanji">睦</div>
                <div class="keyword" style="display: none">intimate</div>
            </div>

            <div class="divTableCell" id="1633">
                <div class="framenr">1633</div>
                <div class="kanji">勢</div>
                <div class="keyword" style="display: none">forces</div>
            </div>

            <div class="divTableCell" id="1634">
                <div class="framenr">1634</div>
                <div class="kanji">熱</div>
                <div class="keyword" style="display: none">heat</div>
            </div>

            <div class="divTableCell" id="1635">
                <div class="framenr">1635</div>
                <div class="kanji">菱</div>
                <div class="keyword" style="display: none">diamond</div>
            </div>

            <div class="divTableCell" id="1636">
                <div class="framenr">1636</div>
                <div class="kanji">陵</div>
                <div class="keyword" style="display: none">mausoleum</div>
            </div>

            <div class="divTableCell" id="1637">
                <div class="framenr">1637</div>
                <div class="kanji">亥</div>
                <div class="keyword" style="display: none">sign of the hog</div>
            </div>

            <div class="divTableCell" id="1638">
                <div class="framenr">1638</div>
                <div class="kanji">核</div>
                <div class="keyword" style="display: none">nucleus</div>
            </div>

            <div class="divTableCell" id="1639">
                <div class="framenr">1639</div>
                <div class="kanji">刻</div>
                <div class="keyword" style="display: none">engrave</div>
            </div>

            <div class="divTableCell" id="1640">
                <div class="framenr">1640</div>
                <div class="kanji">該</div>
                <div class="keyword" style="display: none">above-stated</div>
            </div>

            <div class="divTableCell" id="1641">
                <div class="framenr">1641</div>
                <div class="kanji">骸</div>
                <div class="keyword" style="display: none">remains</div>
            </div>

            <div class="divTableCell" id="1642">
                <div class="framenr">1642</div>
                <div class="kanji">劾</div>
                <div class="keyword" style="display: none">censure</div>
            </div>

            <div class="divTableCell" id="1643">
                <div class="framenr">1643</div>
                <div class="kanji">述</div>
                <div class="keyword" style="display: none">mention</div>
            </div>

            <div class="divTableCell" id="1644">
                <div class="framenr">1644</div>
                <div class="kanji">術</div>
                <div class="keyword" style="display: none">art</div>
            </div>

            <div class="divTableCell" id="1645">
                <div class="framenr">1645</div>
                <div class="kanji">寒</div>
                <div class="keyword" style="display: none">cold</div>
            </div>

            <div class="divTableCell" id="1646">
                <div class="framenr">1646</div>
                <div class="kanji">塞</div>
                <div class="keyword" style="display: none">block up</div>
            </div>

            <div class="divTableCell" id="1647">
                <div class="framenr">1647</div>
                <div class="kanji">醸</div>
                <div class="keyword" style="display: none">brew</div>
            </div>

            <div class="divTableCell" id="1648">
                <div class="framenr">1648</div>
                <div class="kanji">譲</div>
                <div class="keyword" style="display: none">defer</div>
            </div>

            <div class="divTableCell" id="1649">
                <div class="framenr">1649</div>
                <div class="kanji">壌</div>
                <div class="keyword" style="display: none">lot</div>
            </div>

            <div class="divTableCell" id="1650">
                <div class="framenr">1650</div>
                <div class="kanji">嬢</div>
                <div class="keyword" style="display: none">lass</div>
            </div>

            <div class="divTableCell" id="1651">
                <div class="framenr">1651</div>
                <div class="kanji">毒</div>
                <div class="keyword" style="display: none">poison</div>
            </div>

            <div class="divTableCell" id="1652">
                <div class="framenr">1652</div>
                <div class="kanji">素</div>
                <div class="keyword" style="display: none">elementary</div>
            </div>

            <div class="divTableCell" id="1653">
                <div class="framenr">1653</div>
                <div class="kanji">麦</div>
                <div class="keyword" style="display: none">barley</div>
            </div>

            <div class="divTableCell" id="1654">
                <div class="framenr">1654</div>
                <div class="kanji">青</div>
                <div class="keyword" style="display: none">blue</div>
            </div>

            <div class="divTableCell" id="1655">
                <div class="framenr">1655</div>
                <div class="kanji">精</div>
                <div class="keyword" style="display: none">refined</div>
            </div>

            <div class="divTableCell" id="1656">
                <div class="framenr">1656</div>
                <div class="kanji">請</div>
                <div class="keyword" style="display: none">solicit</div>
            </div>

            <div class="divTableCell" id="1657">
                <div class="framenr">1657</div>
                <div class="kanji">情</div>
                <div class="keyword" style="display: none">feelings</div>
            </div>

            <div class="divTableCell" id="1658">
                <div class="framenr">1658</div>
                <div class="kanji">晴</div>
                <div class="keyword" style="display: none">clear up</div>
            </div>

            <div class="divTableCell" id="1659">
                <div class="framenr">1659</div>
                <div class="kanji">清</div>
                <div class="keyword" style="display: none">pure</div>
            </div>

            <div class="divTableCell" id="1660">
                <div class="framenr">1660</div>
                <div class="kanji">静</div>
                <div class="keyword" style="display: none">quiet</div>
            </div>

            <div class="divTableCell" id="1661">
                <div class="framenr">1661</div>
                <div class="kanji">責</div>
                <div class="keyword" style="display: none">blame</div>
            </div>

            <div class="divTableCell" id="1662">
                <div class="framenr">1662</div>
                <div class="kanji">績</div>
                <div class="keyword" style="display: none">exploits</div>
            </div>

            <div class="divTableCell" id="1663">
                <div class="framenr">1663</div>
                <div class="kanji">積</div>
                <div class="keyword" style="display: none">volume</div>
            </div>

            <div class="divTableCell" id="1664">
                <div class="framenr">1664</div>
                <div class="kanji">債</div>
                <div class="keyword" style="display: none">bond</div>
            </div>

            <div class="divTableCell" id="1665">
                <div class="framenr">1665</div>
                <div class="kanji">漬</div>
                <div class="keyword" style="display: none">pickling</div>
            </div>

            <div class="divTableCell" id="1666">
                <div class="framenr">1666</div>
                <div class="kanji">表</div>
                <div class="keyword" style="display: none">surface</div>
            </div>

            <div class="divTableCell" id="1667">
                <div class="framenr">1667</div>
                <div class="kanji">俵</div>
                <div class="keyword" style="display: none">bag</div>
            </div>

            <div class="divTableCell" id="1668">
                <div class="framenr">1668</div>
                <div class="kanji">潔</div>
                <div class="keyword" style="display: none">undefiled</div>
            </div>

            <div class="divTableCell" id="1669">
                <div class="framenr">1669</div>
                <div class="kanji">契</div>
                <div class="keyword" style="display: none">pledge</div>
            </div>

            <div class="divTableCell" id="1670">
                <div class="framenr">1670</div>
                <div class="kanji">喫</div>
                <div class="keyword" style="display: none">consume</div>
            </div>

            <div class="divTableCell" id="1671">
                <div class="framenr">1671</div>
                <div class="kanji">害</div>
                <div class="keyword" style="display: none">harm</div>
            </div>

            <div class="divTableCell" id="1672">
                <div class="framenr">1672</div>
                <div class="kanji">轄</div>
                <div class="keyword" style="display: none">control</div>
            </div>

            <div class="divTableCell" id="1673">
                <div class="framenr">1673</div>
                <div class="kanji">割</div>
                <div class="keyword" style="display: none">proportion</div>
            </div>

            <div class="divTableCell" id="1674">
                <div class="framenr">1674</div>
                <div class="kanji">憲</div>
                <div class="keyword" style="display: none">constitution</div>
            </div>

            <div class="divTableCell" id="1675">
                <div class="framenr">1675</div>
                <div class="kanji">生</div>
                <div class="keyword" style="display: none">life</div>
            </div>

            <div class="divTableCell" id="1676">
                <div class="framenr">1676</div>
                <div class="kanji">星</div>
                <div class="keyword" style="display: none">star</div>
            </div>

            <div class="divTableCell" id="1677">
                <div class="framenr">1677</div>
                <div class="kanji">醒</div>
                <div class="keyword" style="display: none">awakening</div>
            </div>

            <div class="divTableCell" id="1678">
                <div class="framenr">1678</div>
                <div class="kanji">姓</div>
                <div class="keyword" style="display: none">surname</div>
            </div>

            <div class="divTableCell" id="1679">
                <div class="framenr">1679</div>
                <div class="kanji">性</div>
                <div class="keyword" style="display: none">sex</div>
            </div>

            <div class="divTableCell" id="1680">
                <div class="framenr">1680</div>
                <div class="kanji">牲</div>
                <div class="keyword" style="display: none">animal sacrifice</div>
            </div>

            <div class="divTableCell" id="1681">
                <div class="framenr">1681</div>
                <div class="kanji">産</div>
                <div class="keyword" style="display: none">products</div>
            </div>

            <div class="divTableCell" id="1682">
                <div class="framenr">1682</div>
                <div class="kanji">隆</div>
                <div class="keyword" style="display: none">hump</div>
            </div>

            <div class="divTableCell" id="1683">
                <div class="framenr">1683</div>
                <div class="kanji">峰</div>
                <div class="keyword" style="display: none">summit</div>
            </div>

            <div class="divTableCell" id="1684">
                <div class="framenr">1684</div>
                <div class="kanji">蜂</div>
                <div class="keyword" style="display: none">bee</div>
            </div>

            <div class="divTableCell" id="1685">
                <div class="framenr">1685</div>
                <div class="kanji">縫</div>
                <div class="keyword" style="display: none">sew</div>
            </div>

            <div class="divTableCell" id="1686">
                <div class="framenr">1686</div>
                <div class="kanji">拝</div>
                <div class="keyword" style="display: none">worship</div>
            </div>

            <div class="divTableCell" id="1687">
                <div class="framenr">1687</div>
                <div class="kanji">寿</div>
                <div class="keyword" style="display: none">longevity</div>
            </div>

            <div class="divTableCell" id="1688">
                <div class="framenr">1688</div>
                <div class="kanji">鋳</div>
                <div class="keyword" style="display: none">casting</div>
            </div>

            <div class="divTableCell" id="1689">
                <div class="framenr">1689</div>
                <div class="kanji">籍</div>
                <div class="keyword" style="display: none">enroll</div>
            </div>

            <div class="divTableCell" id="1690">
                <div class="framenr">1690</div>
                <div class="kanji">春</div>
                <div class="keyword" style="display: none">springtime</div>
            </div>

            <div class="divTableCell" id="1691">
                <div class="framenr">1691</div>
                <div class="kanji">椿</div>
                <div class="keyword" style="display: none">camellia</div>
            </div>

            <div class="divTableCell" id="1692">
                <div class="framenr">1692</div>
                <div class="kanji">泰</div>
                <div class="keyword" style="display: none">peaceful</div>
            </div>

            <div class="divTableCell" id="1693">
                <div class="framenr">1693</div>
                <div class="kanji">奏</div>
                <div class="keyword" style="display: none">play music</div>
            </div>

            <div class="divTableCell" id="1694">
                <div class="framenr">1694</div>
                <div class="kanji">実</div>
                <div class="keyword" style="display: none">reality</div>
            </div>

            <div class="divTableCell" id="1695">
                <div class="framenr">1695</div>
                <div class="kanji">奉</div>
                <div class="keyword" style="display: none">dedicate</div>
            </div>

            <div class="divTableCell" id="1696">
                <div class="framenr">1696</div>
                <div class="kanji">俸</div>
                <div class="keyword" style="display: none">stipend</div>
            </div>

            <div class="divTableCell" id="1697">
                <div class="framenr">1697</div>
                <div class="kanji">棒</div>
                <div class="keyword" style="display: none">rod</div>
            </div>

            <div class="divTableCell" id="1698">
                <div class="framenr">1698</div>
                <div class="kanji">謹</div>
                <div class="keyword" style="display: none">discreet</div>
            </div>

            <div class="divTableCell" id="1699">
                <div class="framenr">1699</div>
                <div class="kanji">僅</div>
                <div class="keyword" style="display: none">trifle</div>
            </div>

            <div class="divTableCell" id="1700">
                <div class="framenr">1700</div>
                <div class="kanji">勤</div>
                <div class="keyword" style="display: none">diligence</div>
            </div>

            <div class="divTableCell" id="1701">
                <div class="framenr">1701</div>
                <div class="kanji">漢</div>
                <div class="keyword" style="display: none">Sino-</div>
            </div>

            <div class="divTableCell" id="1702">
                <div class="framenr">1702</div>
                <div class="kanji">嘆</div>
                <div class="keyword" style="display: none">sigh</div>
            </div>

            <div class="divTableCell" id="1703">
                <div class="framenr">1703</div>
                <div class="kanji">難</div>
                <div class="keyword" style="display: none">difficult</div>
            </div>

            <div class="divTableCell" id="1704">
                <div class="framenr">1704</div>
                <div class="kanji">華</div>
                <div class="keyword" style="display: none">splendor</div>
            </div>

            <div class="divTableCell" id="1705">
                <div class="framenr">1705</div>
                <div class="kanji">垂</div>
                <div class="keyword" style="display: none">droop</div>
            </div>

            <div class="divTableCell" id="1706">
                <div class="framenr">1706</div>
                <div class="kanji">唾</div>
                <div class="keyword" style="display: none">saliva</div>
            </div>

            <div class="divTableCell" id="1707">
                <div class="framenr">1707</div>
                <div class="kanji">睡</div>
                <div class="keyword" style="display: none">drowsy</div>
            </div>

            <div class="divTableCell" id="1708">
                <div class="framenr">1708</div>
                <div class="kanji">錘</div>
                <div class="keyword" style="display: none">spindle</div>
            </div>

            <div class="divTableCell" id="1709">
                <div class="framenr">1709</div>
                <div class="kanji">乗</div>
                <div class="keyword" style="display: none">ride</div>
            </div>

            <div class="divTableCell" id="1710">
                <div class="framenr">1710</div>
                <div class="kanji">剰</div>
                <div class="keyword" style="display: none">surplus</div>
            </div>

            <div class="divTableCell" id="1711">
                <div class="framenr">1711</div>
                <div class="kanji">今</div>
                <div class="keyword" style="display: none">now</div>
            </div>

            <div class="divTableCell" id="1712">
                <div class="framenr">1712</div>
                <div class="kanji">含</div>
                <div class="keyword" style="display: none">include</div>
            </div>

            <div class="divTableCell" id="1713">
                <div class="framenr">1713</div>
                <div class="kanji">貪</div>
                <div class="keyword" style="display: none">covet</div>
            </div>

            <div class="divTableCell" id="1714">
                <div class="framenr">1714</div>
                <div class="kanji">吟</div>
                <div class="keyword" style="display: none">versify</div>
            </div>

            <div class="divTableCell" id="1715">
                <div class="framenr">1715</div>
                <div class="kanji">念</div>
                <div class="keyword" style="display: none">wish</div>
            </div>

            <div class="divTableCell" id="1716">
                <div class="framenr">1716</div>
                <div class="kanji">捻</div>
                <div class="keyword" style="display: none">wrench</div>
            </div>

            <div class="divTableCell" id="1717">
                <div class="framenr">1717</div>
                <div class="kanji">琴</div>
                <div class="keyword" style="display: none">harp</div>
            </div>

            <div class="divTableCell" id="1718">
                <div class="framenr">1718</div>
                <div class="kanji">陰</div>
                <div class="keyword" style="display: none">shade</div>
            </div>

            <div class="divTableCell" id="1719">
                <div class="framenr">1719</div>
                <div class="kanji">予</div>
                <div class="keyword" style="display: none">beforehand</div>
            </div>

            <div class="divTableCell" id="1720">
                <div class="framenr">1720</div>
                <div class="kanji">序</div>
                <div class="keyword" style="display: none">preface</div>
            </div>

            <div class="divTableCell" id="1721">
                <div class="framenr">1721</div>
                <div class="kanji">預</div>
                <div class="keyword" style="display: none">deposit</div>
            </div>

            <div class="divTableCell" id="1722">
                <div class="framenr">1722</div>
                <div class="kanji">野</div>
                <div class="keyword" style="display: none">plains</div>
            </div>

            <div class="divTableCell" id="1723">
                <div class="framenr">1723</div>
                <div class="kanji">兼</div>
                <div class="keyword" style="display: none">concurrently</div>
            </div>

            <div class="divTableCell" id="1724">
                <div class="framenr">1724</div>
                <div class="kanji">嫌</div>
                <div class="keyword" style="display: none">dislike</div>
            </div>

            <div class="divTableCell" id="1725">
                <div class="framenr">1725</div>
                <div class="kanji">鎌</div>
                <div class="keyword" style="display: none">sickle</div>
            </div>

            <div class="divTableCell" id="1726">
                <div class="framenr">1726</div>
                <div class="kanji">謙</div>
                <div class="keyword" style="display: none">self-effacing</div>
            </div>

            <div class="divTableCell" id="1727">
                <div class="framenr">1727</div>
                <div class="kanji">廉</div>
                <div class="keyword" style="display: none">bargain</div>
            </div>

            <div class="divTableCell" id="1728">
                <div class="framenr">1728</div>
                <div class="kanji">西</div>
                <div class="keyword" style="display: none">west</div>
            </div>

            <div class="divTableCell" id="1729">
                <div class="framenr">1729</div>
                <div class="kanji">価</div>
                <div class="keyword" style="display: none">value</div>
            </div>

            <div class="divTableCell" id="1730">
                <div class="framenr">1730</div>
                <div class="kanji">要</div>
                <div class="keyword" style="display: none">need</div>
            </div>

            <div class="divTableCell" id="1731">
                <div class="framenr">1731</div>
                <div class="kanji">腰</div>
                <div class="keyword" style="display: none">loins</div>
            </div>

            <div class="divTableCell" id="1732">
                <div class="framenr">1732</div>
                <div class="kanji">票</div>
                <div class="keyword" style="display: none">ballot</div>
            </div>

            <div class="divTableCell" id="1733">
                <div class="framenr">1733</div>
                <div class="kanji">漂</div>
                <div class="keyword" style="display: none">drift</div>
            </div>

            <div class="divTableCell" id="1734">
                <div class="framenr">1734</div>
                <div class="kanji">標</div>
                <div class="keyword" style="display: none">signpost</div>
            </div>

            <div class="divTableCell" id="1735">
                <div class="framenr">1735</div>
                <div class="kanji">栗</div>
                <div class="keyword" style="display: none">chestnut</div>
            </div>

            <div class="divTableCell" id="1736">
                <div class="framenr">1736</div>
                <div class="kanji">慄</div>
                <div class="keyword" style="display: none">shudder</div>
            </div>

            <div class="divTableCell" id="1737">
                <div class="framenr">1737</div>
                <div class="kanji">遷</div>
                <div class="keyword" style="display: none">transition</div>
            </div>

            <div class="divTableCell" id="1738">
                <div class="framenr">1738</div>
                <div class="kanji">覆</div>
                <div class="keyword" style="display: none">capsize</div>
            </div>

            <div class="divTableCell" id="1739">
                <div class="framenr">1739</div>
                <div class="kanji">煙</div>
                <div class="keyword" style="display: none">smoke</div>
            </div>

            <div class="divTableCell" id="1740">
                <div class="framenr">1740</div>
                <div class="kanji">南</div>
                <div class="keyword" style="display: none">south</div>
            </div>

            <div class="divTableCell" id="1741">
                <div class="framenr">1741</div>
                <div class="kanji">楠</div>
                <div class="keyword" style="display: none">camphor tree</div>
            </div>

            <div class="divTableCell" id="1742">
                <div class="framenr">1742</div>
                <div class="kanji">献</div>
                <div class="keyword" style="display: none">offering</div>
            </div>

            <div class="divTableCell" id="1743">
                <div class="framenr">1743</div>
                <div class="kanji">門</div>
                <div class="keyword" style="display: none">gates</div>
            </div>

            <div class="divTableCell" id="1744">
                <div class="framenr">1744</div>
                <div class="kanji">問</div>
                <div class="keyword" style="display: none">question</div>
            </div>

            <div class="divTableCell" id="1745">
                <div class="framenr">1745</div>
                <div class="kanji">閲</div>
                <div class="keyword" style="display: none">review</div>
            </div>

            <div class="divTableCell" id="1746">
                <div class="framenr">1746</div>
                <div class="kanji">閥</div>
                <div class="keyword" style="display: none">clique</div>
            </div>

            <div class="divTableCell" id="1747">
                <div class="framenr">1747</div>
                <div class="kanji">間</div>
                <div class="keyword" style="display: none">interval</div>
            </div>

            <div class="divTableCell" id="1748">
                <div class="framenr">1748</div>
                <div class="kanji">闇</div>
                <div class="keyword" style="display: none">pitch dark</div>
            </div>

            <div class="divTableCell" id="1749">
                <div class="framenr">1749</div>
                <div class="kanji">簡</div>
                <div class="keyword" style="display: none">simplicity</div>
            </div>

            <div class="divTableCell" id="1750">
                <div class="framenr">1750</div>
                <div class="kanji">開</div>
                <div class="keyword" style="display: none">open</div>
            </div>

            <div class="divTableCell" id="1751">
                <div class="framenr">1751</div>
                <div class="kanji">閉</div>
                <div class="keyword" style="display: none">closed</div>
            </div>

            <div class="divTableCell" id="1752">
                <div class="framenr">1752</div>
                <div class="kanji">閣</div>
                <div class="keyword" style="display: none">tower</div>
            </div>

            <div class="divTableCell" id="1753">
                <div class="framenr">1753</div>
                <div class="kanji">閑</div>
                <div class="keyword" style="display: none">leisure</div>
            </div>

            <div class="divTableCell" id="1754">
                <div class="framenr">1754</div>
                <div class="kanji">聞</div>
                <div class="keyword" style="display: none">hear</div>
            </div>

            <div class="divTableCell" id="1755">
                <div class="framenr">1755</div>
                <div class="kanji">潤</div>
                <div class="keyword" style="display: none">wet</div>
            </div>

            <div class="divTableCell" id="1756">
                <div class="framenr">1756</div>
                <div class="kanji">欄</div>
                <div class="keyword" style="display: none">column</div>
            </div>

            <div class="divTableCell" id="1757">
                <div class="framenr">1757</div>
                <div class="kanji">闘</div>
                <div class="keyword" style="display: none">fight</div>
            </div>

            <div class="divTableCell" id="1758">
                <div class="framenr">1758</div>
                <div class="kanji">倉</div>
                <div class="keyword" style="display: none">godown</div>
            </div>

            <div class="divTableCell" id="1759">
                <div class="framenr">1759</div>
                <div class="kanji">創</div>
                <div class="keyword" style="display: none">genesis</div>
            </div>

            <div class="divTableCell" id="1760">
                <div class="framenr">1760</div>
                <div class="kanji">非</div>
                <div class="keyword" style="display: none">un-</div>
            </div>

            <div class="divTableCell" id="1761">
                <div class="framenr">1761</div>
                <div class="kanji">俳</div>
                <div class="keyword" style="display: none">haiku</div>
            </div>

            <div class="divTableCell" id="1762">
                <div class="framenr">1762</div>
                <div class="kanji">排</div>
                <div class="keyword" style="display: none">repudiate</div>
            </div>

            <div class="divTableCell" id="1763">
                <div class="framenr">1763</div>
                <div class="kanji">悲</div>
                <div class="keyword" style="display: none">sad</div>
            </div>

            <div class="divTableCell" id="1764">
                <div class="framenr">1764</div>
                <div class="kanji">罪</div>
                <div class="keyword" style="display: none">guilt</div>
            </div>

            <div class="divTableCell" id="1765">
                <div class="framenr">1765</div>
                <div class="kanji">輩</div>
                <div class="keyword" style="display: none">comrade</div>
            </div>

            <div class="divTableCell" id="1766">
                <div class="framenr">1766</div>
                <div class="kanji">扉</div>
                <div class="keyword" style="display: none">front door</div>
            </div>

            <div class="divTableCell" id="1767">
                <div class="framenr">1767</div>
                <div class="kanji">侯</div>
                <div class="keyword" style="display: none">marquis</div>
            </div>

            <div class="divTableCell" id="1768">
                <div class="framenr">1768</div>
                <div class="kanji">喉</div>
                <div class="keyword" style="display: none">throat</div>
            </div>

            <div class="divTableCell" id="1769">
                <div class="framenr">1769</div>
                <div class="kanji">候</div>
                <div class="keyword" style="display: none">climate</div>
            </div>

            <div class="divTableCell" id="1770">
                <div class="framenr">1770</div>
                <div class="kanji">決</div>
                <div class="keyword" style="display: none">decide</div>
            </div>

            <div class="divTableCell" id="1771">
                <div class="framenr">1771</div>
                <div class="kanji">快</div>
                <div class="keyword" style="display: none">cheerful</div>
            </div>

            <div class="divTableCell" id="1772">
                <div class="framenr">1772</div>
                <div class="kanji">偉</div>
                <div class="keyword" style="display: none">admirable</div>
            </div>

            <div class="divTableCell" id="1773">
                <div class="framenr">1773</div>
                <div class="kanji">違</div>
                <div class="keyword" style="display: none">difference</div>
            </div>

            <div class="divTableCell" id="1774">
                <div class="framenr">1774</div>
                <div class="kanji">緯</div>
                <div class="keyword" style="display: none">horizontal</div>
            </div>

            <div class="divTableCell" id="1775">
                <div class="framenr">1775</div>
                <div class="kanji">衛</div>
                <div class="keyword" style="display: none">defense</div>
            </div>

            <div class="divTableCell" id="1776">
                <div class="framenr">1776</div>
                <div class="kanji">韓</div>
                <div class="keyword" style="display: none">Korea</div>
            </div>

            <div class="divTableCell" id="1777">
                <div class="framenr">1777</div>
                <div class="kanji">干</div>
                <div class="keyword" style="display: none">dry</div>
            </div>

            <div class="divTableCell" id="1778">
                <div class="framenr">1778</div>
                <div class="kanji">肝</div>
                <div class="keyword" style="display: none">liver</div>
            </div>

            <div class="divTableCell" id="1779">
                <div class="framenr">1779</div>
                <div class="kanji">刊</div>
                <div class="keyword" style="display: none">publish</div>
            </div>

            <div class="divTableCell" id="1780">
                <div class="framenr">1780</div>
                <div class="kanji">汗</div>
                <div class="keyword" style="display: none">sweat</div>
            </div>

            <div class="divTableCell" id="1781">
                <div class="framenr">1781</div>
                <div class="kanji">軒</div>
                <div class="keyword" style="display: none">flats</div>
            </div>

            <div class="divTableCell" id="1782">
                <div class="framenr">1782</div>
                <div class="kanji">岸</div>
                <div class="keyword" style="display: none">beach</div>
            </div>

            <div class="divTableCell" id="1783">
                <div class="framenr">1783</div>
                <div class="kanji">幹</div>
                <div class="keyword" style="display: none">tree trunk</div>
            </div>

            <div class="divTableCell" id="1784">
                <div class="framenr">1784</div>
                <div class="kanji">芋</div>
                <div class="keyword" style="display: none">potato</div>
            </div>

            <div class="divTableCell" id="1785">
                <div class="framenr">1785</div>
                <div class="kanji">宇</div>
                <div class="keyword" style="display: none">eaves</div>
            </div>

            <div class="divTableCell" id="1786">
                <div class="framenr">1786</div>
                <div class="kanji">余</div>
                <div class="keyword" style="display: none">too much</div>
            </div>

            <div class="divTableCell" id="1787">
                <div class="framenr">1787</div>
                <div class="kanji">除</div>
                <div class="keyword" style="display: none">exclude</div>
            </div>

            <div class="divTableCell" id="1788">
                <div class="framenr">1788</div>
                <div class="kanji">徐</div>
                <div class="keyword" style="display: none">gradually</div>
            </div>

            <div class="divTableCell" id="1789">
                <div class="framenr">1789</div>
                <div class="kanji">叙</div>
                <div class="keyword" style="display: none">confer</div>
            </div>

            <div class="divTableCell" id="1790">
                <div class="framenr">1790</div>
                <div class="kanji">途</div>
                <div class="keyword" style="display: none">route</div>
            </div>

            <div class="divTableCell" id="1791">
                <div class="framenr">1791</div>
                <div class="kanji">斜</div>
                <div class="keyword" style="display: none">diagonal</div>
            </div>

            <div class="divTableCell" id="1792">
                <div class="framenr">1792</div>
                <div class="kanji">塗</div>
                <div class="keyword" style="display: none">paint</div>
            </div>

            <div class="divTableCell" id="1793">
                <div class="framenr">1793</div>
                <div class="kanji">束</div>
                <div class="keyword" style="display: none">bundle</div>
            </div>

            <div class="divTableCell" id="1794">
                <div class="framenr">1794</div>
                <div class="kanji">頼</div>
                <div class="keyword" style="display: none">trust</div>
            </div>

            <div class="divTableCell" id="1795">
                <div class="framenr">1795</div>
                <div class="kanji">瀬</div>
                <div class="keyword" style="display: none">rapids</div>
            </div>

            <div class="divTableCell" id="1796">
                <div class="framenr">1796</div>
                <div class="kanji">勅</div>
                <div class="keyword" style="display: none">imperial order</div>
            </div>

            <div class="divTableCell" id="1797">
                <div class="framenr">1797</div>
                <div class="kanji">疎</div>
                <div class="keyword" style="display: none">alienate</div>
            </div>

            <div class="divTableCell" id="1798">
                <div class="framenr">1798</div>
                <div class="kanji">辣</div>
                <div class="keyword" style="display: none">bitter</div>
            </div>

            <div class="divTableCell" id="1799">
                <div class="framenr">1799</div>
                <div class="kanji">速</div>
                <div class="keyword" style="display: none">quick</div>
            </div>

            <div class="divTableCell" id="1800">
                <div class="framenr">1800</div>
                <div class="kanji">整</div>
                <div class="keyword" style="display: none">organize</div>
            </div>

            <div class="divTableCell" id="1801">
                <div class="framenr">1801</div>
                <div class="kanji">剣</div>
                <div class="keyword" style="display: none">saber</div>
            </div>

            <div class="divTableCell" id="1802">
                <div class="framenr">1802</div>
                <div class="kanji">険</div>
                <div class="keyword" style="display: none">precipitous</div>
            </div>

            <div class="divTableCell" id="1803">
                <div class="framenr">1803</div>
                <div class="kanji">検</div>
                <div class="keyword" style="display: none">examination</div>
            </div>

            <div class="divTableCell" id="1804">
                <div class="framenr">1804</div>
                <div class="kanji">倹</div>
                <div class="keyword" style="display: none">frugal</div>
            </div>

            <div class="divTableCell" id="1805">
                <div class="framenr">1805</div>
                <div class="kanji">重</div>
                <div class="keyword" style="display: none">heavy</div>
            </div>

            <div class="divTableCell" id="1806">
                <div class="framenr">1806</div>
                <div class="kanji">動</div>
                <div class="keyword" style="display: none">move</div>
            </div>

            <div class="divTableCell" id="1807">
                <div class="framenr">1807</div>
                <div class="kanji">腫</div>
                <div class="keyword" style="display: none">tumor</div>
            </div>

            <div class="divTableCell" id="1808">
                <div class="framenr">1808</div>
                <div class="kanji">勲</div>
                <div class="keyword" style="display: none">meritorious deed</div>
            </div>

            <div class="divTableCell" id="1809">
                <div class="framenr">1809</div>
                <div class="kanji">働</div>
                <div class="keyword" style="display: none">work</div>
            </div>

            <div class="divTableCell" id="1810">
                <div class="framenr">1810</div>
                <div class="kanji">種</div>
                <div class="keyword" style="display: none">species</div>
            </div>

            <div class="divTableCell" id="1811">
                <div class="framenr">1811</div>
                <div class="kanji">衝</div>
                <div class="keyword" style="display: none">collide</div>
            </div>

            <div class="divTableCell" id="1812">
                <div class="framenr">1812</div>
                <div class="kanji">薫</div>
                <div class="keyword" style="display: none">fragrant</div>
            </div>

            <div class="divTableCell" id="1813">
                <div class="framenr">1813</div>
                <div class="kanji">病</div>
                <div class="keyword" style="display: none">ill</div>
            </div>

            <div class="divTableCell" id="1814">
                <div class="framenr">1814</div>
                <div class="kanji">痴</div>
                <div class="keyword" style="display: none">stupid</div>
            </div>

            <div class="divTableCell" id="1815">
                <div class="framenr">1815</div>
                <div class="kanji">痘</div>
                <div class="keyword" style="display: none">pox</div>
            </div>

            <div class="divTableCell" id="1816">
                <div class="framenr">1816</div>
                <div class="kanji">症</div>
                <div class="keyword" style="display: none">symptoms</div>
            </div>

            <div class="divTableCell" id="1817">
                <div class="framenr">1817</div>
                <div class="kanji">瘍</div>
                <div class="keyword" style="display: none">carbuncle</div>
            </div>

            <div class="divTableCell" id="1818">
                <div class="framenr">1818</div>
                <div class="kanji">痩</div>
                <div class="keyword" style="display: none">lose weight</div>
            </div>

            <div class="divTableCell" id="1819">
                <div class="framenr">1819</div>
                <div class="kanji">疾</div>
                <div class="keyword" style="display: none">rapidly</div>
            </div>

            <div class="divTableCell" id="1820">
                <div class="framenr">1820</div>
                <div class="kanji">嫉</div>
                <div class="keyword" style="display: none">envy</div>
            </div>

            <div class="divTableCell" id="1821">
                <div class="framenr">1821</div>
                <div class="kanji">痢</div>
                <div class="keyword" style="display: none">diarrhea</div>
            </div>

            <div class="divTableCell" id="1822">
                <div class="framenr">1822</div>
                <div class="kanji">痕</div>
                <div class="keyword" style="display: none">scar</div>
            </div>

            <div class="divTableCell" id="1823">
                <div class="framenr">1823</div>
                <div class="kanji">疲</div>
                <div class="keyword" style="display: none">tired</div>
            </div>

            <div class="divTableCell" id="1824">
                <div class="framenr">1824</div>
                <div class="kanji">疫</div>
                <div class="keyword" style="display: none">epidemic</div>
            </div>

            <div class="divTableCell" id="1825">
                <div class="framenr">1825</div>
                <div class="kanji">痛</div>
                <div class="keyword" style="display: none">pain</div>
            </div>

            <div class="divTableCell" id="1826">
                <div class="framenr">1826</div>
                <div class="kanji">癖</div>
                <div class="keyword" style="display: none">mannerism</div>
            </div>

            <div class="divTableCell" id="1827">
                <div class="framenr">1827</div>
                <div class="kanji">匿</div>
                <div class="keyword" style="display: none">hide</div>
            </div>

            <div class="divTableCell" id="1828">
                <div class="framenr">1828</div>
                <div class="kanji">匠</div>
                <div class="keyword" style="display: none">artisan</div>
            </div>

            <div class="divTableCell" id="1829">
                <div class="framenr">1829</div>
                <div class="kanji">医</div>
                <div class="keyword" style="display: none">doctor</div>
            </div>

            <div class="divTableCell" id="1830">
                <div class="framenr">1830</div>
                <div class="kanji">匹</div>
                <div class="keyword" style="display: none">equal</div>
            </div>

            <div class="divTableCell" id="1831">
                <div class="framenr">1831</div>
                <div class="kanji">区</div>
                <div class="keyword" style="display: none">ward</div>
            </div>

            <div class="divTableCell" id="1832">
                <div class="framenr">1832</div>
                <div class="kanji">枢</div>
                <div class="keyword" style="display: none">hinge</div>
            </div>

            <div class="divTableCell" id="1833">
                <div class="framenr">1833</div>
                <div class="kanji">殴</div>
                <div class="keyword" style="display: none">assault</div>
            </div>

            <div class="divTableCell" id="1834">
                <div class="framenr">1834</div>
                <div class="kanji">欧</div>
                <div class="keyword" style="display: none">Europe</div>
            </div>

            <div class="divTableCell" id="1835">
                <div class="framenr">1835</div>
                <div class="kanji">抑</div>
                <div class="keyword" style="display: none">repress</div>
            </div>

            <div class="divTableCell" id="1836">
                <div class="framenr">1836</div>
                <div class="kanji">仰</div>
                <div class="keyword" style="display: none">faceup</div>
            </div>

            <div class="divTableCell" id="1837">
                <div class="framenr">1837</div>
                <div class="kanji">迎</div>
                <div class="keyword" style="display: none">welcome</div>
            </div>

            <div class="divTableCell" id="1838">
                <div class="framenr">1838</div>
                <div class="kanji">登</div>
                <div class="keyword" style="display: none">ascend</div>
            </div>

            <div class="divTableCell" id="1839">
                <div class="framenr">1839</div>
                <div class="kanji">澄</div>
                <div class="keyword" style="display: none">lucidity</div>
            </div>

            <div class="divTableCell" id="1840">
                <div class="framenr">1840</div>
                <div class="kanji">発</div>
                <div class="keyword" style="display: none">discharge</div>
            </div>

            <div class="divTableCell" id="1841">
                <div class="framenr">1841</div>
                <div class="kanji">廃</div>
                <div class="keyword" style="display: none">abolish</div>
            </div>

            <div class="divTableCell" id="1842">
                <div class="framenr">1842</div>
                <div class="kanji">僚</div>
                <div class="keyword" style="display: none">colleague</div>
            </div>

            <div class="divTableCell" id="1843">
                <div class="framenr">1843</div>
                <div class="kanji">瞭</div>
                <div class="keyword" style="display: none">obvious</div>
            </div>

            <div class="divTableCell" id="1844">
                <div class="framenr">1844</div>
                <div class="kanji">寮</div>
                <div class="keyword" style="display: none">dormitory</div>
            </div>

            <div class="divTableCell" id="1845">
                <div class="framenr">1845</div>
                <div class="kanji">療</div>
                <div class="keyword" style="display: none">heal</div>
            </div>

            <div class="divTableCell" id="1846">
                <div class="framenr">1846</div>
                <div class="kanji">彫</div>
                <div class="keyword" style="display: none">carve(blender)</div>
            </div>

            <div class="divTableCell" id="1847">
                <div class="framenr">1847</div>
                <div class="kanji">形</div>
                <div class="keyword" style="display: none">shape</div>
            </div>

            <div class="divTableCell" id="1848">
                <div class="framenr">1848</div>
                <div class="kanji">影</div>
                <div class="keyword" style="display: none">shadow</div>
            </div>

            <div class="divTableCell" id="1849">
                <div class="framenr">1849</div>
                <div class="kanji">杉</div>
                <div class="keyword" style="display: none">cedar</div>
            </div>

            <div class="divTableCell" id="1850">
                <div class="framenr">1850</div>
                <div class="kanji">彩</div>
                <div class="keyword" style="display: none">coloring</div>
            </div>

            <div class="divTableCell" id="1851">
                <div class="framenr">1851</div>
                <div class="kanji">彰</div>
                <div class="keyword" style="display: none">patent</div>
            </div>

            <div class="divTableCell" id="1852">
                <div class="framenr">1852</div>
                <div class="kanji">彦</div>
                <div class="keyword" style="display: none">lad</div>
            </div>

            <div class="divTableCell" id="1853">
                <div class="framenr">1853</div>
                <div class="kanji">顔</div>
                <div class="keyword" style="display: none">face</div>
            </div>

            <div class="divTableCell" id="1854">
                <div class="framenr">1854</div>
                <div class="kanji">須</div>
                <div class="keyword" style="display: none">ought</div>
            </div>

            <div class="divTableCell" id="1855">
                <div class="framenr">1855</div>
                <div class="kanji">膨</div>
                <div class="keyword" style="display: none">swell</div>
            </div>

            <div class="divTableCell" id="1856">
                <div class="framenr">1856</div>
                <div class="kanji">参</div>
                <div class="keyword" style="display: none">visit</div>
            </div>

            <div class="divTableCell" id="1857">
                <div class="framenr">1857</div>
                <div class="kanji">惨</div>
                <div class="keyword" style="display: none">wretched</div>
            </div>

            <div class="divTableCell" id="1858">
                <div class="framenr">1858</div>
                <div class="kanji">修</div>
                <div class="keyword" style="display: none">discipline</div>
            </div>

            <div class="divTableCell" id="1859">
                <div class="framenr">1859</div>
                <div class="kanji">珍</div>
                <div class="keyword" style="display: none">rare</div>
            </div>

            <div class="divTableCell" id="1860">
                <div class="framenr">1860</div>
                <div class="kanji">診</div>
                <div class="keyword" style="display: none">checkup</div>
            </div>

            <div class="divTableCell" id="1861">
                <div class="framenr">1861</div>
                <div class="kanji">文</div>
                <div class="keyword" style="display: none">sentence</div>
            </div>

            <div class="divTableCell" id="1862">
                <div class="framenr">1862</div>
                <div class="kanji">対</div>
                <div class="keyword" style="display: none">vis-a-vis</div>
            </div>

            <div class="divTableCell" id="1863">
                <div class="framenr">1863</div>
                <div class="kanji">紋</div>
                <div class="keyword" style="display: none">family crest</div>
            </div>

            <div class="divTableCell" id="1864">
                <div class="framenr">1864</div>
                <div class="kanji">蚊</div>
                <div class="keyword" style="display: none">mosquito</div>
            </div>

            <div class="divTableCell" id="1865">
                <div class="framenr">1865</div>
                <div class="kanji">斑</div>
                <div class="keyword" style="display: none">speckled</div>
            </div>

            <div class="divTableCell" id="1866">
                <div class="framenr">1866</div>
                <div class="kanji">斉</div>
                <div class="keyword" style="display: none">adjusted</div>
            </div>

            <div class="divTableCell" id="1867">
                <div class="framenr">1867</div>
                <div class="kanji">剤</div>
                <div class="keyword" style="display: none">dose</div>
            </div>

            <div class="divTableCell" id="1868">
                <div class="framenr">1868</div>
                <div class="kanji">済</div>
                <div class="keyword" style="display: none">finish</div>
            </div>

            <div class="divTableCell" id="1869">
                <div class="framenr">1869</div>
                <div class="kanji">斎</div>
                <div class="keyword" style="display: none">purification</div>
            </div>

            <div class="divTableCell" id="1870">
                <div class="framenr">1870</div>
                <div class="kanji">粛</div>
                <div class="keyword" style="display: none">solemn</div>
            </div>

            <div class="divTableCell" id="1871">
                <div class="framenr">1871</div>
                <div class="kanji">塁</div>
                <div class="keyword" style="display: none">bases</div>
            </div>

            <div class="divTableCell" id="1872">
                <div class="framenr">1872</div>
                <div class="kanji">楽</div>
                <div class="keyword" style="display: none">music</div>
            </div>

            <div class="divTableCell" id="1873">
                <div class="framenr">1873</div>
                <div class="kanji">薬</div>
                <div class="keyword" style="display: none">medicine</div>
            </div>

            <div class="divTableCell" id="1874">
                <div class="framenr">1874</div>
                <div class="kanji">率</div>
                <div class="keyword" style="display: none">ratio</div>
            </div>

            <div class="divTableCell" id="1875">
                <div class="framenr">1875</div>
                <div class="kanji">渋</div>
                <div class="keyword" style="display: none">astringent</div>
            </div>

            <div class="divTableCell" id="1876">
                <div class="framenr">1876</div>
                <div class="kanji">摂</div>
                <div class="keyword" style="display: none">vicarious</div>
            </div>

            <div class="divTableCell" id="1877">
                <div class="framenr">1877</div>
                <div class="kanji">央</div>
                <div class="keyword" style="display: none">center</div>
            </div>

            <div class="divTableCell" id="1878">
                <div class="framenr">1878</div>
                <div class="kanji">英</div>
                <div class="keyword" style="display: none">England</div>
            </div>

            <div class="divTableCell" id="1879">
                <div class="framenr">1879</div>
                <div class="kanji">映</div>
                <div class="keyword" style="display: none">reflect</div>
            </div>

            <div class="divTableCell" id="1880">
                <div class="framenr">1880</div>
                <div class="kanji">赤</div>
                <div class="keyword" style="display: none">red</div>
            </div>

            <div class="divTableCell" id="1881">
                <div class="framenr">1881</div>
                <div class="kanji">赦</div>
                <div class="keyword" style="display: none">pardon</div>
            </div>

            <div class="divTableCell" id="1882">
                <div class="framenr">1882</div>
                <div class="kanji">変</div>
                <div class="keyword" style="display: none">unusual</div>
            </div>

            <div class="divTableCell" id="1883">
                <div class="framenr">1883</div>
                <div class="kanji">跡</div>
                <div class="keyword" style="display: none">tracks</div>
            </div>

            <div class="divTableCell" id="1884">
                <div class="framenr">1884</div>
                <div class="kanji">蛮</div>
                <div class="keyword" style="display: none">barbarian</div>
            </div>

            <div class="divTableCell" id="1885">
                <div class="framenr">1885</div>
                <div class="kanji">恋</div>
                <div class="keyword" style="display: none">romance</div>
            </div>

            <div class="divTableCell" id="1886">
                <div class="framenr">1886</div>
                <div class="kanji">湾</div>
                <div class="keyword" style="display: none">gulf</div>
            </div>

            <div class="divTableCell" id="1887">
                <div class="framenr">1887</div>
                <div class="kanji">黄</div>
                <div class="keyword" style="display: none">yellow</div>
            </div>

            <div class="divTableCell" id="1888">
                <div class="framenr">1888</div>
                <div class="kanji">横</div>
                <div class="keyword" style="display: none">sideways</div>
            </div>

            <div class="divTableCell" id="1889">
                <div class="framenr">1889</div>
                <div class="kanji">把</div>
                <div class="keyword" style="display: none">grasp</div>
            </div>

            <div class="divTableCell" id="1890">
                <div class="framenr">1890</div>
                <div class="kanji">色</div>
                <div class="keyword" style="display: none">color</div>
            </div>

            <div class="divTableCell" id="1891">
                <div class="framenr">1891</div>
                <div class="kanji">絶</div>
                <div class="keyword" style="display: none">discontinue</div>
            </div>

            <div class="divTableCell" id="1892">
                <div class="framenr">1892</div>
                <div class="kanji">艶</div>
                <div class="keyword" style="display: none">glossy</div>
            </div>

            <div class="divTableCell" id="1893">
                <div class="framenr">1893</div>
                <div class="kanji">肥</div>
                <div class="keyword" style="display: none">fertilizer</div>
            </div>

            <div class="divTableCell" id="1894">
                <div class="framenr">1894</div>
                <div class="kanji">甘</div>
                <div class="keyword" style="display: none">sweet</div>
            </div>

            <div class="divTableCell" id="1895">
                <div class="framenr">1895</div>
                <div class="kanji">紺</div>
                <div class="keyword" style="display: none">navy blue</div>
            </div>

            <div class="divTableCell" id="1896">
                <div class="framenr">1896</div>
                <div class="kanji">某</div>
                <div class="keyword" style="display: none">so-and-so</div>
            </div>

            <div class="divTableCell" id="1897">
                <div class="framenr">1897</div>
                <div class="kanji">謀</div>
                <div class="keyword" style="display: none">conspire</div>
            </div>

            <div class="divTableCell" id="1898">
                <div class="framenr">1898</div>
                <div class="kanji">媒</div>
                <div class="keyword" style="display: none">mediator</div>
            </div>

            <div class="divTableCell" id="1899">
                <div class="framenr">1899</div>
                <div class="kanji">欺</div>
                <div class="keyword" style="display: none">deceit</div>
            </div>

            <div class="divTableCell" id="1900">
                <div class="framenr">1900</div>
                <div class="kanji">棋</div>
                <div class="keyword" style="display: none">chess piece</div>
            </div>

            <div class="divTableCell" id="1901">
                <div class="framenr">1901</div>
                <div class="kanji">旗</div>
                <div class="keyword" style="display: none">national flag</div>
            </div>

            <div class="divTableCell" id="1902">
                <div class="framenr">1902</div>
                <div class="kanji">期</div>
                <div class="keyword" style="display: none">period</div>
            </div>

            <div class="divTableCell" id="1903">
                <div class="framenr">1903</div>
                <div class="kanji">碁</div>
                <div class="keyword" style="display: none">Go</div>
            </div>

            <div class="divTableCell" id="1904">
                <div class="framenr">1904</div>
                <div class="kanji">基</div>
                <div class="keyword" style="display: none">fundamentals</div>
            </div>

            <div class="divTableCell" id="1905">
                <div class="framenr">1905</div>
                <div class="kanji">甚</div>
                <div class="keyword" style="display: none">tremendously</div>
            </div>

            <div class="divTableCell" id="1906">
                <div class="framenr">1906</div>
                <div class="kanji">勘</div>
                <div class="keyword" style="display: none">intuition</div>
            </div>

            <div class="divTableCell" id="1907">
                <div class="framenr">1907</div>
                <div class="kanji">堪</div>
                <div class="keyword" style="display: none">withstand</div>
            </div>

            <div class="divTableCell" id="1908">
                <div class="framenr">1908</div>
                <div class="kanji">貴</div>
                <div class="keyword" style="display: none">precious</div>
            </div>

            <div class="divTableCell" id="1909">
                <div class="framenr">1909</div>
                <div class="kanji">遺</div>
                <div class="keyword" style="display: none">bequeath</div>
            </div>

            <div class="divTableCell" id="1910">
                <div class="framenr">1910</div>
                <div class="kanji">遣</div>
                <div class="keyword" style="display: none">dispatch</div>
            </div>

            <div class="divTableCell" id="1911">
                <div class="framenr">1911</div>
                <div class="kanji">潰</div>
                <div class="keyword" style="display: none">defile</div>
            </div>

            <div class="divTableCell" id="1912">
                <div class="framenr">1912</div>
                <div class="kanji">舞</div>
                <div class="keyword" style="display: none">dance</div>
            </div>

            <div class="divTableCell" id="1913">
                <div class="framenr">1913</div>
                <div class="kanji">無</div>
                <div class="keyword" style="display: none">nothingness</div>
            </div>

            <div class="divTableCell" id="1914">
                <div class="framenr">1914</div>
                <div class="kanji">組</div>
                <div class="keyword" style="display: none">association</div>
            </div>

            <div class="divTableCell" id="1915">
                <div class="framenr">1915</div>
                <div class="kanji">粗</div>
                <div class="keyword" style="display: none">coarse</div>
            </div>

            <div class="divTableCell" id="1916">
                <div class="framenr">1916</div>
                <div class="kanji">租</div>
                <div class="keyword" style="display: none">tariff</div>
            </div>

            <div class="divTableCell" id="1917">
                <div class="framenr">1917</div>
                <div class="kanji">狙</div>
                <div class="keyword" style="display: none">aim at</div>
            </div>

            <div class="divTableCell" id="1918">
                <div class="framenr">1918</div>
                <div class="kanji">祖</div>
                <div class="keyword" style="display: none">ancestor</div>
            </div>

            <div class="divTableCell" id="1919">
                <div class="framenr">1919</div>
                <div class="kanji">阻</div>
                <div class="keyword" style="display: none">thwart</div>
            </div>

            <div class="divTableCell" id="1920">
                <div class="framenr">1920</div>
                <div class="kanji">査</div>
                <div class="keyword" style="display: none">investigate</div>
            </div>

            <div class="divTableCell" id="1921">
                <div class="framenr">1921</div>
                <div class="kanji">助</div>
                <div class="keyword" style="display: none">help</div>
            </div>

            <div class="divTableCell" id="1922">
                <div class="framenr">1922</div>
                <div class="kanji">宜</div>
                <div class="keyword" style="display: none">best regards</div>
            </div>

            <div class="divTableCell" id="1923">
                <div class="framenr">1923</div>
                <div class="kanji">畳</div>
                <div class="keyword" style="display: none">tatami mat</div>
            </div>

            <div class="divTableCell" id="1924">
                <div class="framenr">1924</div>
                <div class="kanji">並</div>
                <div class="keyword" style="display: none">row</div>
            </div>

            <div class="divTableCell" id="1925">
                <div class="framenr">1925</div>
                <div class="kanji">普</div>
                <div class="keyword" style="display: none">universal</div>
            </div>

            <div class="divTableCell" id="1926">
                <div class="framenr">1926</div>
                <div class="kanji">譜</div>
                <div class="keyword" style="display: none">musical score</div>
            </div>

            <div class="divTableCell" id="1927">
                <div class="framenr">1927</div>
                <div class="kanji">湿</div>
                <div class="keyword" style="display: none">damp</div>
            </div>

            <div class="divTableCell" id="1928">
                <div class="framenr">1928</div>
                <div class="kanji">顕</div>
                <div class="keyword" style="display: none">appear</div>
            </div>

            <div class="divTableCell" id="1929">
                <div class="framenr">1929</div>
                <div class="kanji">繊</div>
                <div class="keyword" style="display: none">slender</div>
            </div>

            <div class="divTableCell" id="1930">
                <div class="framenr">1930</div>
                <div class="kanji">霊</div>
                <div class="keyword" style="display: none">spirits</div>
            </div>

            <div class="divTableCell" id="1931">
                <div class="framenr">1931</div>
                <div class="kanji">業</div>
                <div class="keyword" style="display: none">profession</div>
            </div>

            <div class="divTableCell" id="1932">
                <div class="framenr">1932</div>
                <div class="kanji">撲</div>
                <div class="keyword" style="display: none">slap</div>
            </div>

            <div class="divTableCell" id="1933">
                <div class="framenr">1933</div>
                <div class="kanji">僕</div>
                <div class="keyword" style="display: none">me</div>
            </div>

            <div class="divTableCell" id="1934">
                <div class="framenr">1934</div>
                <div class="kanji">共</div>
                <div class="keyword" style="display: none">together</div>
            </div>

            <div class="divTableCell" id="1935">
                <div class="framenr">1935</div>
                <div class="kanji">供</div>
                <div class="keyword" style="display: none">submit</div>
            </div>

            <div class="divTableCell" id="1936">
                <div class="framenr">1936</div>
                <div class="kanji">異</div>
                <div class="keyword" style="display: none">uncommon</div>
            </div>

            <div class="divTableCell" id="1937">
                <div class="framenr">1937</div>
                <div class="kanji">翼</div>
                <div class="keyword" style="display: none">wing</div>
            </div>

            <div class="divTableCell" id="1938">
                <div class="framenr">1938</div>
                <div class="kanji">戴</div>
                <div class="keyword" style="display: none">accept humbly</div>
            </div>

            <div class="divTableCell" id="1939">
                <div class="framenr">1939</div>
                <div class="kanji">洪</div>
                <div class="keyword" style="display: none">deluge</div>
            </div>

            <div class="divTableCell" id="1940">
                <div class="framenr">1940</div>
                <div class="kanji">港</div>
                <div class="keyword" style="display: none">harbor</div>
            </div>

            <div class="divTableCell" id="1941">
                <div class="framenr">1941</div>
                <div class="kanji">暴</div>
                <div class="keyword" style="display: none">outburst</div>
            </div>

            <div class="divTableCell" id="1942">
                <div class="framenr">1942</div>
                <div class="kanji">爆</div>
                <div class="keyword" style="display: none">bomb</div>
            </div>

            <div class="divTableCell" id="1943">
                <div class="framenr">1943</div>
                <div class="kanji">恭</div>
                <div class="keyword" style="display: none">respect</div>
            </div>

            <div class="divTableCell" id="1944">
                <div class="framenr">1944</div>
                <div class="kanji">選</div>
                <div class="keyword" style="display: none">elect</div>
            </div>

            <div class="divTableCell" id="1945">
                <div class="framenr">1945</div>
                <div class="kanji">殿</div>
                <div class="keyword" style="display: none">Mr.</div>
            </div>

            <div class="divTableCell" id="1946">
                <div class="framenr">1946</div>
                <div class="kanji">井</div>
                <div class="keyword" style="display: none">well</div>
            </div>

            <div class="divTableCell" id="1947">
                <div class="framenr">1947</div>
                <div class="kanji">丼</div>
                <div class="keyword" style="display: none">donburi</div>
            </div>

            <div class="divTableCell" id="1948">
                <div class="framenr">1948</div>
                <div class="kanji">囲</div>
                <div class="keyword" style="display: none">surround</div>
            </div>

            <div class="divTableCell" id="1949">
                <div class="framenr">1949</div>
                <div class="kanji">耕</div>
                <div class="keyword" style="display: none">till</div>
            </div>

            <div class="divTableCell" id="1950">
                <div class="framenr">1950</div>
                <div class="kanji">亜</div>
                <div class="keyword" style="display: none">Asia</div>
            </div>

            <div class="divTableCell" id="1951">
                <div class="framenr">1951</div>
                <div class="kanji">悪</div>
                <div class="keyword" style="display: none">bad</div>
            </div>

            <div class="divTableCell" id="1952">
                <div class="framenr">1952</div>
                <div class="kanji">円</div>
                <div class="keyword" style="display: none">circle</div>
            </div>

            <div class="divTableCell" id="1953">
                <div class="framenr">1953</div>
                <div class="kanji">角</div>
                <div class="keyword" style="display: none">angle</div>
            </div>

            <div class="divTableCell" id="1954">
                <div class="framenr">1954</div>
                <div class="kanji">触</div>
                <div class="keyword" style="display: none">contact</div>
            </div>

            <div class="divTableCell" id="1955">
                <div class="framenr">1955</div>
                <div class="kanji">解</div>
                <div class="keyword" style="display: none">unravel</div>
            </div>

            <div class="divTableCell" id="1956">
                <div class="framenr">1956</div>
                <div class="kanji">再</div>
                <div class="keyword" style="display: none">again</div>
            </div>

            <div class="divTableCell" id="1957">
                <div class="framenr">1957</div>
                <div class="kanji">講</div>
                <div class="keyword" style="display: none">lecture</div>
            </div>

            <div class="divTableCell" id="1958">
                <div class="framenr">1958</div>
                <div class="kanji">購</div>
                <div class="keyword" style="display: none">subscription</div>
            </div>

            <div class="divTableCell" id="1959">
                <div class="framenr">1959</div>
                <div class="kanji">構</div>
                <div class="keyword" style="display: none">posture</div>
            </div>

            <div class="divTableCell" id="1960">
                <div class="framenr">1960</div>
                <div class="kanji">溝</div>
                <div class="keyword" style="display: none">gutter</div>
            </div>

            <div class="divTableCell" id="1961">
                <div class="framenr">1961</div>
                <div class="kanji">論</div>
                <div class="keyword" style="display: none">argument</div>
            </div>

            <div class="divTableCell" id="1962">
                <div class="framenr">1962</div>
                <div class="kanji">倫</div>
                <div class="keyword" style="display: none">ethics</div>
            </div>

            <div class="divTableCell" id="1963">
                <div class="framenr">1963</div>
                <div class="kanji">輪</div>
                <div class="keyword" style="display: none">wheel</div>
            </div>

            <div class="divTableCell" id="1964">
                <div class="framenr">1964</div>
                <div class="kanji">偏</div>
                <div class="keyword" style="display: none">partial</div>
            </div>

            <div class="divTableCell" id="1965">
                <div class="framenr">1965</div>
                <div class="kanji">遍</div>
                <div class="keyword" style="display: none">everywhere</div>
            </div>

            <div class="divTableCell" id="1966">
                <div class="framenr">1966</div>
                <div class="kanji">編</div>
                <div class="keyword" style="display: none">compilation</div>
            </div>

            <div class="divTableCell" id="1967">
                <div class="framenr">1967</div>
                <div class="kanji">冊</div>
                <div class="keyword" style="display: none">tome</div>
            </div>

            <div class="divTableCell" id="1968">
                <div class="framenr">1968</div>
                <div class="kanji">柵</div>
                <div class="keyword" style="display: none">palisade</div>
            </div>

            <div class="divTableCell" id="1969">
                <div class="framenr">1969</div>
                <div class="kanji">典</div>
                <div class="keyword" style="display: none">code</div>
            </div>

            <div class="divTableCell" id="1970">
                <div class="framenr">1970</div>
                <div class="kanji">氏</div>
                <div class="keyword" style="display: none">family name</div>
            </div>

            <div class="divTableCell" id="1971">
                <div class="framenr">1971</div>
                <div class="kanji">紙</div>
                <div class="keyword" style="display: none">paper</div>
            </div>

            <div class="divTableCell" id="1972">
                <div class="framenr">1972</div>
                <div class="kanji">婚</div>
                <div class="keyword" style="display: none">marriage</div>
            </div>

            <div class="divTableCell" id="1973">
                <div class="framenr">1973</div>
                <div class="kanji">低</div>
                <div class="keyword" style="display: none">lower</div>
            </div>

            <div class="divTableCell" id="1974">
                <div class="framenr">1974</div>
                <div class="kanji">抵</div>
                <div class="keyword" style="display: none">resist</div>
            </div>

            <div class="divTableCell" id="1975">
                <div class="framenr">1975</div>
                <div class="kanji">底</div>
                <div class="keyword" style="display: none">bottom</div>
            </div>

            <div class="divTableCell" id="1976">
                <div class="framenr">1976</div>
                <div class="kanji">民</div>
                <div class="keyword" style="display: none">people</div>
            </div>

            <div class="divTableCell" id="1977">
                <div class="framenr">1977</div>
                <div class="kanji">眠</div>
                <div class="keyword" style="display: none">sleep</div>
            </div>

            <div class="divTableCell" id="1978">
                <div class="framenr">1978</div>
                <div class="kanji">捕</div>
                <div class="keyword" style="display: none">catch</div>
            </div>

            <div class="divTableCell" id="1979">
                <div class="framenr">1979</div>
                <div class="kanji">哺</div>
                <div class="keyword" style="display: none">suckle</div>
            </div>

            <div class="divTableCell" id="1980">
                <div class="framenr">1980</div>
                <div class="kanji">浦</div>
                <div class="keyword" style="display: none">bay</div>
            </div>

            <div class="divTableCell" id="1981">
                <div class="framenr">1981</div>
                <div class="kanji">蒲</div>
                <div class="keyword" style="display: none">bullrush</div>
            </div>

            <div class="divTableCell" id="1982">
                <div class="framenr">1982</div>
                <div class="kanji">舗</div>
                <div class="keyword" style="display: none">shop</div>
            </div>

            <div class="divTableCell" id="1983">
                <div class="framenr">1983</div>
                <div class="kanji">補</div>
                <div class="keyword" style="display: none">supplement</div>
            </div>

            <div class="divTableCell" id="1984">
                <div class="framenr">1984</div>
                <div class="kanji">邸</div>
                <div class="keyword" style="display: none">residence</div>
            </div>

            <div class="divTableCell" id="1985">
                <div class="framenr">1985</div>
                <div class="kanji">郭</div>
                <div class="keyword" style="display: none">enclosure</div>
            </div>

            <div class="divTableCell" id="1986">
                <div class="framenr">1986</div>
                <div class="kanji">郡</div>
                <div class="keyword" style="display: none">county</div>
            </div>

            <div class="divTableCell" id="1987">
                <div class="framenr">1987</div>
                <div class="kanji">郊</div>
                <div class="keyword" style="display: none">outskirts</div>
            </div>

            <div class="divTableCell" id="1988">
                <div class="framenr">1988</div>
                <div class="kanji">部</div>
                <div class="keyword" style="display: none">section</div>
            </div>

            <div class="divTableCell" id="1989">
                <div class="framenr">1989</div>
                <div class="kanji">都</div>
                <div class="keyword" style="display: none">metropolis</div>
            </div>

            <div class="divTableCell" id="1990">
                <div class="framenr">1990</div>
                <div class="kanji">郵</div>
                <div class="keyword" style="display: none">mail</div>
            </div>

            <div class="divTableCell" id="1991">
                <div class="framenr">1991</div>
                <div class="kanji">邦</div>
                <div class="keyword" style="display: none">home country</div>
            </div>

            <div class="divTableCell" id="1992">
                <div class="framenr">1992</div>
                <div class="kanji">那</div>
                <div class="keyword" style="display: none">interrogative</div>
            </div>

            <div class="divTableCell" id="1993">
                <div class="framenr">1993</div>
                <div class="kanji">郷</div>
                <div class="keyword" style="display: none">hometown</div>
            </div>

            <div class="divTableCell" id="1994">
                <div class="framenr">1994</div>
                <div class="kanji">響</div>
                <div class="keyword" style="display: none">echo</div>
            </div>

            <div class="divTableCell" id="1995">
                <div class="framenr">1995</div>
                <div class="kanji">郎</div>
                <div class="keyword" style="display: none">son</div>
            </div>

            <div class="divTableCell" id="1996">
                <div class="framenr">1996</div>
                <div class="kanji">廊</div>
                <div class="keyword" style="display: none">corridor</div>
            </div>

            <div class="divTableCell" id="1997">
                <div class="framenr">1997</div>
                <div class="kanji">盾</div>
                <div class="keyword" style="display: none">shield</div>
            </div>

            <div class="divTableCell" id="1998">
                <div class="framenr">1998</div>
                <div class="kanji">循</div>
                <div class="keyword" style="display: none">sequential</div>
            </div>

            <div class="divTableCell" id="1999">
                <div class="framenr">1999</div>
                <div class="kanji">派</div>
                <div class="keyword" style="display: none">faction</div>
            </div>

            <div class="divTableCell" id="2000">
                <div class="framenr">2000</div>
                <div class="kanji">脈</div>
                <div class="keyword" style="display: none">vein</div>
            </div>

            <div class="divTableCell" id="2001">
                <div class="framenr">2001</div>
                <div class="kanji">衆</div>
                <div class="keyword" style="display: none">masses</div>
            </div>

            <div class="divTableCell" id="2002">
                <div class="framenr">2002</div>
                <div class="kanji">逓</div>
                <div class="keyword" style="display: none">parcel post</div>
            </div>

            <div class="divTableCell" id="2003">
                <div class="framenr">2003</div>
                <div class="kanji">段</div>
                <div class="keyword" style="display: none">grade</div>
            </div>

            <div class="divTableCell" id="2004">
                <div class="framenr">2004</div>
                <div class="kanji">鍛</div>
                <div class="keyword" style="display: none">forge</div>
            </div>

            <div class="divTableCell" id="2005">
                <div class="framenr">2005</div>
                <div class="kanji">后</div>
                <div class="keyword" style="display: none">empress</div>
            </div>

            <div class="divTableCell" id="2006">
                <div class="framenr">2006</div>
                <div class="kanji">幻</div>
                <div class="keyword" style="display: none">phantasm</div>
            </div>

            <div class="divTableCell" id="2007">
                <div class="framenr">2007</div>
                <div class="kanji">司</div>
                <div class="keyword" style="display: none">director</div>
            </div>

            <div class="divTableCell" id="2008">
                <div class="framenr">2008</div>
                <div class="kanji">伺</div>
                <div class="keyword" style="display: none">pay respects</div>
            </div>

            <div class="divTableCell" id="2009">
                <div class="framenr">2009</div>
                <div class="kanji">詞</div>
                <div class="keyword" style="display: none">parts of speech</div>
            </div>

            <div class="divTableCell" id="2010">
                <div class="framenr">2010</div>
                <div class="kanji">飼</div>
                <div class="keyword" style="display: none">domesticate</div>
            </div>

            <div class="divTableCell" id="2011">
                <div class="framenr">2011</div>
                <div class="kanji">嗣</div>
                <div class="keyword" style="display: none">heir</div>
            </div>

            <div class="divTableCell" id="2012">
                <div class="framenr">2012</div>
                <div class="kanji">舟</div>
                <div class="keyword" style="display: none">boat</div>
            </div>

            <div class="divTableCell" id="2013">
                <div class="framenr">2013</div>
                <div class="kanji">舶</div>
                <div class="keyword" style="display: none">liner</div>
            </div>

            <div class="divTableCell" id="2014">
                <div class="framenr">2014</div>
                <div class="kanji">航</div>
                <div class="keyword" style="display: none">navigate</div>
            </div>

            <div class="divTableCell" id="2015">
                <div class="framenr">2015</div>
                <div class="kanji">舷</div>
                <div class="keyword" style="display: none">gunwale</div>
            </div>

            <div class="divTableCell" id="2016">
                <div class="framenr">2016</div>
                <div class="kanji">般</div>
                <div class="keyword" style="display: none">carrier</div>
            </div>

            <div class="divTableCell" id="2017">
                <div class="framenr">2017</div>
                <div class="kanji">盤</div>
                <div class="keyword" style="display: none">tray</div>
            </div>

            <div class="divTableCell" id="2018">
                <div class="framenr">2018</div>
                <div class="kanji">搬</div>
                <div class="keyword" style="display: none">conveyor</div>
            </div>

            <div class="divTableCell" id="2019">
                <div class="framenr">2019</div>
                <div class="kanji">船</div>
                <div class="keyword" style="display: none">ship</div>
            </div>

            <div class="divTableCell" id="2020">
                <div class="framenr">2020</div>
                <div class="kanji">艦</div>
                <div class="keyword" style="display: none">warship</div>
            </div>

            <div class="divTableCell" id="2021">
                <div class="framenr">2021</div>
                <div class="kanji">艇</div>
                <div class="keyword" style="display: none">rowboat</div>
            </div>

            <div class="divTableCell" id="2022">
                <div class="framenr">2022</div>
                <div class="kanji">瓜</div>
                <div class="keyword" style="display: none">melon</div>
            </div>

            <div class="divTableCell" id="2023">
                <div class="framenr">2023</div>
                <div class="kanji">弧</div>
                <div class="keyword" style="display: none">arc</div>
            </div>

            <div class="divTableCell" id="2024">
                <div class="framenr">2024</div>
                <div class="kanji">孤</div>
                <div class="keyword" style="display: none">orphan</div>
            </div>

            <div class="divTableCell" id="2025">
                <div class="framenr">2025</div>
                <div class="kanji">繭</div>
                <div class="keyword" style="display: none">cocoon</div>
            </div>

            <div class="divTableCell" id="2026">
                <div class="framenr">2026</div>
                <div class="kanji">益</div>
                <div class="keyword" style="display: none">benefit</div>
            </div>

            <div class="divTableCell" id="2027">
                <div class="framenr">2027</div>
                <div class="kanji">暇</div>
                <div class="keyword" style="display: none">spare time</div>
            </div>

            <div class="divTableCell" id="2028">
                <div class="framenr">2028</div>
                <div class="kanji">敷</div>
                <div class="keyword" style="display: none">spread</div>
            </div>

            <div class="divTableCell" id="2029">
                <div class="framenr">2029</div>
                <div class="kanji">来</div>
                <div class="keyword" style="display: none">come</div>
            </div>

            <div class="divTableCell" id="2030">
                <div class="framenr">2030</div>
                <div class="kanji">気</div>
                <div class="keyword" style="display: none">spirit</div>
            </div>

            <div class="divTableCell" id="2031">
                <div class="framenr">2031</div>
                <div class="kanji">汽</div>
                <div class="keyword" style="display: none">vapor</div>
            </div>

            <div class="divTableCell" id="2032">
                <div class="framenr">2032</div>
                <div class="kanji">飛</div>
                <div class="keyword" style="display: none">fly</div>
            </div>

            <div class="divTableCell" id="2033">
                <div class="framenr">2033</div>
                <div class="kanji">沈</div>
                <div class="keyword" style="display: none">sink</div>
            </div>

            <div class="divTableCell" id="2034">
                <div class="framenr">2034</div>
                <div class="kanji">枕</div>
                <div class="keyword" style="display: none">pillow</div>
            </div>

            <div class="divTableCell" id="2035">
                <div class="framenr">2035</div>
                <div class="kanji">妻</div>
                <div class="keyword" style="display: none">wife</div>
            </div>

            <div class="divTableCell" id="2036">
                <div class="framenr">2036</div>
                <div class="kanji">凄</div>
                <div class="keyword" style="display: none">nifty</div>
            </div>

            <div class="divTableCell" id="2037">
                <div class="framenr">2037</div>
                <div class="kanji">衰</div>
                <div class="keyword" style="display: none">decline</div>
            </div>

            <div class="divTableCell" id="2038">
                <div class="framenr">2038</div>
                <div class="kanji">衷</div>
                <div class="keyword" style="display: none">inmost</div>
            </div>

            <div class="divTableCell" id="2039">
                <div class="framenr">2039</div>
                <div class="kanji">面</div>
                <div class="keyword" style="display: none">mask</div>
            </div>

            <div class="divTableCell" id="2040">
                <div class="framenr">2040</div>
                <div class="kanji">麺</div>
                <div class="keyword" style="display: none">noodles</div>
            </div>

            <div class="divTableCell" id="2041">
                <div class="framenr">2041</div>
                <div class="kanji">革</div>
                <div class="keyword" style="display: none">leather</div>
            </div>

            <div class="divTableCell" id="2042">
                <div class="framenr">2042</div>
                <div class="kanji">靴</div>
                <div class="keyword" style="display: none">shoes</div>
            </div>

            <div class="divTableCell" id="2043">
                <div class="framenr">2043</div>
                <div class="kanji">覇</div>
                <div class="keyword" style="display: none">hegemony</div>
            </div>

            <div class="divTableCell" id="2044">
                <div class="framenr">2044</div>
                <div class="kanji">声</div>
                <div class="keyword" style="display: none">voice</div>
            </div>

            <div class="divTableCell" id="2045">
                <div class="framenr">2045</div>
                <div class="kanji">眉</div>
                <div class="keyword" style="display: none">eyebrow</div>
            </div>

            <div class="divTableCell" id="2046">
                <div class="framenr">2046</div>
                <div class="kanji">呉</div>
                <div class="keyword" style="display: none">give</div>
            </div>

            <div class="divTableCell" id="2047">
                <div class="framenr">2047</div>
                <div class="kanji">娯</div>
                <div class="keyword" style="display: none">recreation</div>
            </div>

            <div class="divTableCell" id="2048">
                <div class="framenr">2048</div>
                <div class="kanji">誤</div>
                <div class="keyword" style="display: none">mistake</div>
            </div>

            <div class="divTableCell" id="2049">
                <div class="framenr">2049</div>
                <div class="kanji">蒸</div>
                <div class="keyword" style="display: none">steam</div>
            </div>

            <div class="divTableCell" id="2050">
                <div class="framenr">2050</div>
                <div class="kanji">承</div>
                <div class="keyword" style="display: none">acquiesce</div>
            </div>

            <div class="divTableCell" id="2051">
                <div class="framenr">2051</div>
                <div class="kanji">函</div>
                <div class="keyword" style="display: none">bin</div>
            </div>

            <div class="divTableCell" id="2052">
                <div class="framenr">2052</div>
                <div class="kanji">極</div>
                <div class="keyword" style="display: none">poles</div>
            </div>

            <div class="divTableCell" id="2053">
                <div class="framenr">2053</div>
                <div class="kanji">牙</div>
                <div class="keyword" style="display: none">tusk</div>
            </div>

            <div class="divTableCell" id="2054">
                <div class="framenr">2054</div>
                <div class="kanji">芽</div>
                <div class="keyword" style="display: none">bud,sprout</div>
            </div>

            <div class="divTableCell" id="2055">
                <div class="framenr">2055</div>
                <div class="kanji">邪</div>
                <div class="keyword" style="display: none">wicked</div>
            </div>

            <div class="divTableCell" id="2056">
                <div class="framenr">2056</div>
                <div class="kanji">雅</div>
                <div class="keyword" style="display: none">gracious</div>
            </div>

            <div class="divTableCell" id="2057">
                <div class="framenr">2057</div>
                <div class="kanji">釈</div>
                <div class="keyword" style="display: none">interpretation</div>
            </div>

            <div class="divTableCell" id="2058">
                <div class="framenr">2058</div>
                <div class="kanji">番</div>
                <div class="keyword" style="display: none">turn</div>
            </div>

            <div class="divTableCell" id="2059">
                <div class="framenr">2059</div>
                <div class="kanji">審</div>
                <div class="keyword" style="display: none">hearing</div>
            </div>

            <div class="divTableCell" id="2060">
                <div class="framenr">2060</div>
                <div class="kanji">翻</div>
                <div class="keyword" style="display: none">flip</div>
            </div>

            <div class="divTableCell" id="2061">
                <div class="framenr">2061</div>
                <div class="kanji">藩</div>
                <div class="keyword" style="display: none">clan</div>
            </div>

            <div class="divTableCell" id="2062">
                <div class="framenr">2062</div>
                <div class="kanji">毛</div>
                <div class="keyword" style="display: none">fur</div>
            </div>

            <div class="divTableCell" id="2063">
                <div class="framenr">2063</div>
                <div class="kanji">耗</div>
                <div class="keyword" style="display: none">decrease</div>
            </div>

            <div class="divTableCell" id="2064">
                <div class="framenr">2064</div>
                <div class="kanji">尾</div>
                <div class="keyword" style="display: none">tail</div>
            </div>

            <div class="divTableCell" id="2065">
                <div class="framenr">2065</div>
                <div class="kanji">宅</div>
                <div class="keyword" style="display: none">home</div>
            </div>

            <div class="divTableCell" id="2066">
                <div class="framenr">2066</div>
                <div class="kanji">託</div>
                <div class="keyword" style="display: none">consign</div>
            </div>

            <div class="divTableCell" id="2067">
                <div class="framenr">2067</div>
                <div class="kanji">為</div>
                <div class="keyword" style="display: none">do</div>
            </div>

            <div class="divTableCell" id="2068">
                <div class="framenr">2068</div>
                <div class="kanji">偽</div>
                <div class="keyword" style="display: none">falsehood</div>
            </div>

            <div class="divTableCell" id="2069">
                <div class="framenr">2069</div>
                <div class="kanji">畏</div>
                <div class="keyword" style="display: none">apprehensive</div>
            </div>

            <div class="divTableCell" id="2070">
                <div class="framenr">2070</div>
                <div class="kanji">長</div>
                <div class="keyword" style="display: none">long</div>
            </div>

            <div class="divTableCell" id="2071">
                <div class="framenr">2071</div>
                <div class="kanji">張</div>
                <div class="keyword" style="display: none">lengthen</div>
            </div>

            <div class="divTableCell" id="2072">
                <div class="framenr">2072</div>
                <div class="kanji">帳</div>
                <div class="keyword" style="display: none">notebook</div>
            </div>

            <div class="divTableCell" id="2073">
                <div class="framenr">2073</div>
                <div class="kanji">脹</div>
                <div class="keyword" style="display: none">dilate</div>
            </div>

            <div class="divTableCell" id="2074">
                <div class="framenr">2074</div>
                <div class="kanji">髪</div>
                <div class="keyword" style="display: none">hair of the head</div>
            </div>

            <div class="divTableCell" id="2075">
                <div class="framenr">2075</div>
                <div class="kanji">展</div>
                <div class="keyword" style="display: none">unfold</div>
            </div>

            <div class="divTableCell" id="2076">
                <div class="framenr">2076</div>
                <div class="kanji">喪</div>
                <div class="keyword" style="display: none">miss</div>
            </div>

            <div class="divTableCell" id="2077">
                <div class="framenr">2077</div>
                <div class="kanji">巣</div>
                <div class="keyword" style="display: none">nest</div>
            </div>

            <div class="divTableCell" id="2078">
                <div class="framenr">2078</div>
                <div class="kanji">単</div>
                <div class="keyword" style="display: none">simple</div>
            </div>

            <div class="divTableCell" id="2079">
                <div class="framenr">2079</div>
                <div class="kanji">戦</div>
                <div class="keyword" style="display: none">war</div>
            </div>

            <div class="divTableCell" id="2080">
                <div class="framenr">2080</div>
                <div class="kanji">禅</div>
                <div class="keyword" style="display: none">Zen</div>
            </div>

            <div class="divTableCell" id="2081">
                <div class="framenr">2081</div>
                <div class="kanji">弾</div>
                <div class="keyword" style="display: none">bullet</div>
            </div>

            <div class="divTableCell" id="2082">
                <div class="framenr">2082</div>
                <div class="kanji">桜</div>
                <div class="keyword" style="display: none">cherry tree</div>
            </div>

            <div class="divTableCell" id="2083">
                <div class="framenr">2083</div>
                <div class="kanji">獣</div>
                <div class="keyword" style="display: none">animal</div>
            </div>

            <div class="divTableCell" id="2084">
                <div class="framenr">2084</div>
                <div class="kanji">脳</div>
                <div class="keyword" style="display: none">brain</div>
            </div>

            <div class="divTableCell" id="2085">
                <div class="framenr">2085</div>
                <div class="kanji">悩</div>
                <div class="keyword" style="display: none">trouble</div>
            </div>

            <div class="divTableCell" id="2086">
                <div class="framenr">2086</div>
                <div class="kanji">厳</div>
                <div class="keyword" style="display: none">stern</div>
            </div>

            <div class="divTableCell" id="2087">
                <div class="framenr">2087</div>
                <div class="kanji">鎖</div>
                <div class="keyword" style="display: none">chain</div>
            </div>

            <div class="divTableCell" id="2088">
                <div class="framenr">2088</div>
                <div class="kanji">挙</div>
                <div class="keyword" style="display: none">raise</div>
            </div>

            <div class="divTableCell" id="2089">
                <div class="framenr">2089</div>
                <div class="kanji">誉</div>
                <div class="keyword" style="display: none">reputation</div>
            </div>

            <div class="divTableCell" id="2090">
                <div class="framenr">2090</div>
                <div class="kanji">猟</div>
                <div class="keyword" style="display: none">game hunting</div>
            </div>

            <div class="divTableCell" id="2091">
                <div class="framenr">2091</div>
                <div class="kanji">鳥</div>
                <div class="keyword" style="display: none">bird</div>
            </div>

            <div class="divTableCell" id="2092">
                <div class="framenr">2092</div>
                <div class="kanji">鳴</div>
                <div class="keyword" style="display: none">chirp</div>
            </div>

            <div class="divTableCell" id="2093">
                <div class="framenr">2093</div>
                <div class="kanji">鶴</div>
                <div class="keyword" style="display: none">crane</div>
            </div>

            <div class="divTableCell" id="2094">
                <div class="framenr">2094</div>
                <div class="kanji">烏</div>
                <div class="keyword" style="display: none">crow</div>
            </div>

            <div class="divTableCell" id="2095">
                <div class="framenr">2095</div>
                <div class="kanji">蔦</div>
                <div class="keyword" style="display: none">vine</div>
            </div>

            <div class="divTableCell" id="2096">
                <div class="framenr">2096</div>
                <div class="kanji">鳩</div>
                <div class="keyword" style="display: none">pigeon</div>
            </div>

            <div class="divTableCell" id="2097">
                <div class="framenr">2097</div>
                <div class="kanji">鶏</div>
                <div class="keyword" style="display: none">chicken</div>
            </div>

            <div class="divTableCell" id="2098">
                <div class="framenr">2098</div>
                <div class="kanji">島</div>
                <div class="keyword" style="display: none">island</div>
            </div>

            <div class="divTableCell" id="2099">
                <div class="framenr">2099</div>
                <div class="kanji">暖</div>
                <div class="keyword" style="display: none">warmth</div>
            </div>

            <div class="divTableCell" id="2100">
                <div class="framenr">2100</div>
                <div class="kanji">媛</div>
                <div class="keyword" style="display: none">beautiful woman</div>
            </div>

            <div class="divTableCell" id="2101">
                <div class="framenr">2101</div>
                <div class="kanji">援</div>
                <div class="keyword" style="display: none">abet</div>
            </div>

            <div class="divTableCell" id="2102">
                <div class="framenr">2102</div>
                <div class="kanji">緩</div>
                <div class="keyword" style="display: none">slacken</div>
            </div>

            <div class="divTableCell" id="2103">
                <div class="framenr">2103</div>
                <div class="kanji">属</div>
                <div class="keyword" style="display: none">belong</div>
            </div>

            <div class="divTableCell" id="2104">
                <div class="framenr">2104</div>
                <div class="kanji">嘱</div>
                <div class="keyword" style="display: none">entrust</div>
            </div>

            <div class="divTableCell" id="2105">
                <div class="framenr">2105</div>
                <div class="kanji">偶</div>
                <div class="keyword" style="display: none">accidentally</div>
            </div>

            <div class="divTableCell" id="2106">
                <div class="framenr">2106</div>
                <div class="kanji">遇</div>
                <div class="keyword" style="display: none">interview</div>
            </div>

            <div class="divTableCell" id="2107">
                <div class="framenr">2107</div>
                <div class="kanji">愚</div>
                <div class="keyword" style="display: none">foolish</div>
            </div>

            <div class="divTableCell" id="2108">
                <div class="framenr">2108</div>
                <div class="kanji">隅</div>
                <div class="keyword" style="display: none">corner</div>
            </div>

            <div class="divTableCell" id="2109">
                <div class="framenr">2109</div>
                <div class="kanji">逆</div>
                <div class="keyword" style="display: none">inverted</div>
            </div>

            <div class="divTableCell" id="2110">
                <div class="framenr">2110</div>
                <div class="kanji">塑</div>
                <div class="keyword" style="display: none">model</div>
            </div>

            <div class="divTableCell" id="2111">
                <div class="framenr">2111</div>
                <div class="kanji">遡</div>
                <div class="keyword" style="display: none">go upstream</div>
            </div>

            <div class="divTableCell" id="2112">
                <div class="framenr">2112</div>
                <div class="kanji">岡</div>
                <div class="keyword" style="display: none">Mount</div>
            </div>

            <div class="divTableCell" id="2113">
                <div class="framenr">2113</div>
                <div class="kanji">鋼</div>
                <div class="keyword" style="display: none">steel</div>
            </div>

            <div class="divTableCell" id="2114">
                <div class="framenr">2114</div>
                <div class="kanji">綱</div>
                <div class="keyword" style="display: none">hawser</div>
            </div>

            <div class="divTableCell" id="2115">
                <div class="framenr">2115</div>
                <div class="kanji">剛</div>
                <div class="keyword" style="display: none">sturdy</div>
            </div>

            <div class="divTableCell" id="2116">
                <div class="framenr">2116</div>
                <div class="kanji">缶</div>
                <div class="keyword" style="display: none">tin can</div>
            </div>

            <div class="divTableCell" id="2117">
                <div class="framenr">2117</div>
                <div class="kanji">陶</div>
                <div class="keyword" style="display: none">pottery</div>
            </div>

            <div class="divTableCell" id="2118">
                <div class="framenr">2118</div>
                <div class="kanji">揺</div>
                <div class="keyword" style="display: none">swing</div>
            </div>

            <div class="divTableCell" id="2119">
                <div class="framenr">2119</div>
                <div class="kanji">謡</div>
                <div class="keyword" style="display: none">Noh chanting</div>
            </div>

            <div class="divTableCell" id="2120">
                <div class="framenr">2120</div>
                <div class="kanji">鬱</div>
                <div class="keyword" style="display: none">gloom</div>
            </div>

            <div class="divTableCell" id="2121">
                <div class="framenr">2121</div>
                <div class="kanji">就</div>
                <div class="keyword" style="display: none">concerning</div>
            </div>

            <div class="divTableCell" id="2122">
                <div class="framenr">2122</div>
                <div class="kanji">蹴</div>
                <div class="keyword" style="display: none">kick</div>
            </div>

            <div class="divTableCell" id="2123">
                <div class="framenr">2123</div>
                <div class="kanji">懇</div>
                <div class="keyword" style="display: none">sociable</div>
            </div>

            <div class="divTableCell" id="2124">
                <div class="framenr">2124</div>
                <div class="kanji">墾</div>
                <div class="keyword" style="display: none">groundbreaking</div>
            </div>

            <div class="divTableCell" id="2125">
                <div class="framenr">2125</div>
                <div class="kanji">貌</div>
                <div class="keyword" style="display: none">countenance</div>
            </div>

            <div class="divTableCell" id="2126">
                <div class="framenr">2126</div>
                <div class="kanji">免</div>
                <div class="keyword" style="display: none">excuse</div>
            </div>

            <div class="divTableCell" id="2127">
                <div class="framenr">2127</div>
                <div class="kanji">逸</div>
                <div class="keyword" style="display: none">elude</div>
            </div>

            <div class="divTableCell" id="2128">
                <div class="framenr">2128</div>
                <div class="kanji">晩</div>
                <div class="keyword" style="display: none">nightfall</div>
            </div>

            <div class="divTableCell" id="2129">
                <div class="framenr">2129</div>
                <div class="kanji">勉</div>
                <div class="keyword" style="display: none">exertion</div>
            </div>

            <div class="divTableCell" id="2130">
                <div class="framenr">2130</div>
                <div class="kanji">象</div>
                <div class="keyword" style="display: none">elephant</div>
            </div>

            <div class="divTableCell" id="2131">
                <div class="framenr">2131</div>
                <div class="kanji">像</div>
                <div class="keyword" style="display: none">statue</div>
            </div>

            <div class="divTableCell" id="2132">
                <div class="framenr">2132</div>
                <div class="kanji">馬</div>
                <div class="keyword" style="display: none">horse</div>
            </div>

            <div class="divTableCell" id="2133">
                <div class="framenr">2133</div>
                <div class="kanji">駒</div>
                <div class="keyword" style="display: none">pony</div>
            </div>

            <div class="divTableCell" id="2134">
                <div class="framenr">2134</div>
                <div class="kanji">験</div>
                <div class="keyword" style="display: none">verification</div>
            </div>

            <div class="divTableCell" id="2135">
                <div class="framenr">2135</div>
                <div class="kanji">騎</div>
                <div class="keyword" style="display: none">equestrian</div>
            </div>

            <div class="divTableCell" id="2136">
                <div class="framenr">2136</div>
                <div class="kanji">駐</div>
                <div class="keyword" style="display: none">parking</div>
            </div>

            <div class="divTableCell" id="2137">
                <div class="framenr">2137</div>
                <div class="kanji">駆</div>
                <div class="keyword" style="display: none">drive</div>
            </div>

            <div class="divTableCell" id="2138">
                <div class="framenr">2138</div>
                <div class="kanji">駅</div>
                <div class="keyword" style="display: none">station</div>
            </div>

            <div class="divTableCell" id="2139">
                <div class="framenr">2139</div>
                <div class="kanji">騒</div>
                <div class="keyword" style="display: none">boisterous</div>
            </div>

            <div class="divTableCell" id="2140">
                <div class="framenr">2140</div>
                <div class="kanji">駄</div>
                <div class="keyword" style="display: none">burdensome</div>
            </div>

            <div class="divTableCell" id="2141">
                <div class="framenr">2141</div>
                <div class="kanji">驚</div>
                <div class="keyword" style="display: none">wonder</div>
            </div>

            <div class="divTableCell" id="2142">
                <div class="framenr">2142</div>
                <div class="kanji">篤</div>
                <div class="keyword" style="display: none">fervent</div>
            </div>

            <div class="divTableCell" id="2143">
                <div class="framenr">2143</div>
                <div class="kanji">罵</div>
                <div class="keyword" style="display: none">insult</div>
            </div>

            <div class="divTableCell" id="2144">
                <div class="framenr">2144</div>
                <div class="kanji">騰</div>
                <div class="keyword" style="display: none">inflation</div>
            </div>

            <div class="divTableCell" id="2145">
                <div class="framenr">2145</div>
                <div class="kanji">虎</div>
                <div class="keyword" style="display: none">tiger</div>
            </div>

            <div class="divTableCell" id="2146">
                <div class="framenr">2146</div>
                <div class="kanji">虜</div>
                <div class="keyword" style="display: none">captive</div>
            </div>

            <div class="divTableCell" id="2147">
                <div class="framenr">2147</div>
                <div class="kanji">膚</div>
                <div class="keyword" style="display: none">skin</div>
            </div>

            <div class="divTableCell" id="2148">
                <div class="framenr">2148</div>
                <div class="kanji">虚</div>
                <div class="keyword" style="display: none">void</div>
            </div>

            <div class="divTableCell" id="2149">
                <div class="framenr">2149</div>
                <div class="kanji">戯</div>
                <div class="keyword" style="display: none">frolic</div>
            </div>

            <div class="divTableCell" id="2150">
                <div class="framenr">2150</div>
                <div class="kanji">虞</div>
                <div class="keyword" style="display: none">uneasiness</div>
            </div>

            <div class="divTableCell" id="2151">
                <div class="framenr">2151</div>
                <div class="kanji">慮</div>
                <div class="keyword" style="display: none">prudence</div>
            </div>

            <div class="divTableCell" id="2152">
                <div class="framenr">2152</div>
                <div class="kanji">劇</div>
                <div class="keyword" style="display: none">drama</div>
            </div>

            <div class="divTableCell" id="2153">
                <div class="framenr">2153</div>
                <div class="kanji">虐</div>
                <div class="keyword" style="display: none">tyrannize</div>
            </div>

            <div class="divTableCell" id="2154">
                <div class="framenr">2154</div>
                <div class="kanji">鹿</div>
                <div class="keyword" style="display: none">deer</div>
            </div>

            <div class="divTableCell" id="2155">
                <div class="framenr">2155</div>
                <div class="kanji">麓</div>
                <div class="keyword" style="display: none">foot of a mountain</div>
            </div>

            <div class="divTableCell" id="2156">
                <div class="framenr">2156</div>
                <div class="kanji">薦</div>
                <div class="keyword" style="display: none">recommend</div>
            </div>

            <div class="divTableCell" id="2157">
                <div class="framenr">2157</div>
                <div class="kanji">慶</div>
                <div class="keyword" style="display: none">jubilation</div>
            </div>

            <div class="divTableCell" id="2158">
                <div class="framenr">2158</div>
                <div class="kanji">麗</div>
                <div class="keyword" style="display: none">lovely</div>
            </div>

            <div class="divTableCell" id="2159">
                <div class="framenr">2159</div>
                <div class="kanji">熊</div>
                <div class="keyword" style="display: none">bear</div>
            </div>

            <div class="divTableCell" id="2160">
                <div class="framenr">2160</div>
                <div class="kanji">能</div>
                <div class="keyword" style="display: none">ability</div>
            </div>

            <div class="divTableCell" id="2161">
                <div class="framenr">2161</div>
                <div class="kanji">態</div>
                <div class="keyword" style="display: none">attitude</div>
            </div>

            <div class="divTableCell" id="2162">
                <div class="framenr">2162</div>
                <div class="kanji">寅</div>
                <div class="keyword" style="display: none">sign of the tiger</div>
            </div>

            <div class="divTableCell" id="2163">
                <div class="framenr">2163</div>
                <div class="kanji">演</div>
                <div class="keyword" style="display: none">performance</div>
            </div>

            <div class="divTableCell" id="2164">
                <div class="framenr">2164</div>
                <div class="kanji">辰</div>
                <div class="keyword" style="display: none">sign of the dragon</div>
            </div>

            <div class="divTableCell" id="2165">
                <div class="framenr">2165</div>
                <div class="kanji">辱</div>
                <div class="keyword" style="display: none">embarrass</div>
            </div>

            <div class="divTableCell" id="2166">
                <div class="framenr">2166</div>
                <div class="kanji">震</div>
                <div class="keyword" style="display: none">quake</div>
            </div>

            <div class="divTableCell" id="2167">
                <div class="framenr">2167</div>
                <div class="kanji">振</div>
                <div class="keyword" style="display: none">shake</div>
            </div>

            <div class="divTableCell" id="2168">
                <div class="framenr">2168</div>
                <div class="kanji">娠</div>
                <div class="keyword" style="display: none">with child</div>
            </div>

            <div class="divTableCell" id="2169">
                <div class="framenr">2169</div>
                <div class="kanji">唇</div>
                <div class="keyword" style="display: none">lips</div>
            </div>

            <div class="divTableCell" id="2170">
                <div class="framenr">2170</div>
                <div class="kanji">農</div>
                <div class="keyword" style="display: none">agriculture</div>
            </div>

            <div class="divTableCell" id="2171">
                <div class="framenr">2171</div>
                <div class="kanji">濃</div>
                <div class="keyword" style="display: none">concentrated</div>
            </div>

            <div class="divTableCell" id="2172">
                <div class="framenr">2172</div>
                <div class="kanji">送</div>
                <div class="keyword" style="display: none">send off</div>
            </div>

            <div class="divTableCell" id="2173">
                <div class="framenr">2173</div>
                <div class="kanji">関</div>
                <div class="keyword" style="display: none">connection</div>
            </div>

            <div class="divTableCell" id="2174">
                <div class="framenr">2174</div>
                <div class="kanji">咲</div>
                <div class="keyword" style="display: none">blossom</div>
            </div>

            <div class="divTableCell" id="2175">
                <div class="framenr">2175</div>
                <div class="kanji">鬼</div>
                <div class="keyword" style="display: none">ghost</div>
            </div>

            <div class="divTableCell" id="2176">
                <div class="framenr">2176</div>
                <div class="kanji">醜</div>
                <div class="keyword" style="display: none">ugly</div>
            </div>

            <div class="divTableCell" id="2177">
                <div class="framenr">2177</div>
                <div class="kanji">魂</div>
                <div class="keyword" style="display: none">soul</div>
            </div>

            <div class="divTableCell" id="2178">
                <div class="framenr">2178</div>
                <div class="kanji">魔</div>
                <div class="keyword" style="display: none">witch</div>
            </div>

            <div class="divTableCell" id="2179">
                <div class="framenr">2179</div>
                <div class="kanji">魅</div>
                <div class="keyword" style="display: none">fascination</div>
            </div>

            <div class="divTableCell" id="2180">
                <div class="framenr">2180</div>
                <div class="kanji">塊</div>
                <div class="keyword" style="display: none">clod</div>
            </div>

            <div class="divTableCell" id="2181">
                <div class="framenr">2181</div>
                <div class="kanji">襲</div>
                <div class="keyword" style="display: none">attack</div>
            </div>

            <div class="divTableCell" id="2182">
                <div class="framenr">2182</div>
                <div class="kanji">嚇</div>
                <div class="keyword" style="display: none">upbraid</div>
            </div>

            <div class="divTableCell" id="2183">
                <div class="framenr">2183</div>
                <div class="kanji">朕</div>
                <div class="keyword" style="display: none">majestic plural</div>
            </div>

            <div class="divTableCell" id="2184">
                <div class="framenr">2184</div>
                <div class="kanji">雰</div>
                <div class="keyword" style="display: none">atmosphere</div>
            </div>

            <div class="divTableCell" id="2185">
                <div class="framenr">2185</div>
                <div class="kanji">箇</div>
                <div class="keyword" style="display: none">item</div>
            </div>

            <div class="divTableCell" id="2186">
                <div class="framenr">2186</div>
                <div class="kanji">錬</div>
                <div class="keyword" style="display: none">tempering</div>
            </div>

            <div class="divTableCell" id="2187">
                <div class="framenr">2187</div>
                <div class="kanji">遵</div>
                <div class="keyword" style="display: none">abide by</div>
            </div>

            <div class="divTableCell" id="2188">
                <div class="framenr">2188</div>
                <div class="kanji">罷</div>
                <div class="keyword" style="display: none">quit</div>
            </div>

            <div class="divTableCell" id="2189">
                <div class="framenr">2189</div>
                <div class="kanji">屯</div>
                <div class="keyword" style="display: none">barracks</div>
            </div>

            <div class="divTableCell" id="2190">
                <div class="framenr">2190</div>
                <div class="kanji">且</div>
                <div class="keyword" style="display: none">moreover</div>
            </div>

            <div class="divTableCell" id="2191">
                <div class="framenr">2191</div>
                <div class="kanji">藻</div>
                <div class="keyword" style="display: none">seaweed</div>
            </div>

            <div class="divTableCell" id="2192">
                <div class="framenr">2192</div>
                <div class="kanji">隷</div>
                <div class="keyword" style="display: none">slave</div>
            </div>

            <div class="divTableCell" id="2193">
                <div class="framenr">2193</div>
                <div class="kanji">癒</div>
                <div class="keyword" style="display: none">healing</div>
            </div>

            <div class="divTableCell" id="2194">
                <div class="framenr">2194</div>
                <div class="kanji">璽</div>
                <div class="keyword" style="display: none">imperial seal</div>
            </div>

            <div class="divTableCell" id="2195">
                <div class="framenr">2195</div>
                <div class="kanji">潟</div>
                <div class="keyword" style="display: none">lagoon</div>
            </div>

            <div class="divTableCell" id="2196">
                <div class="framenr">2196</div>
                <div class="kanji">丹</div>
                <div class="keyword" style="display: none">cinnabar</div>
            </div>

            <div class="divTableCell" id="2197">
                <div class="framenr">2197</div>
                <div class="kanji">丑</div>
                <div class="keyword" style="display: none">sign of the cow</div>
            </div>

            <div class="divTableCell" id="2198">
                <div class="framenr">2198</div>
                <div class="kanji">羞</div>
                <div class="keyword" style="display: none">humiliate</div>
            </div>

            <div class="divTableCell" id="2199">
                <div class="framenr">2199</div>
                <div class="kanji">卯</div>
                <div class="keyword" style="display: none">sign of the hare</div>
            </div>

            <div class="divTableCell" id="2200">
                <div class="framenr">2200</div>
                <div class="kanji">巳</div>
                <div class="keyword" style="display: none">sign of the snake</div>
            </div>

            <div class="divTableCell" id="2201">
                <div class="framenr">2201</div>
                <div class="kanji">此</div>
                <div class="keyword" style="display: none">this here</div>
            </div>

            <div class="divTableCell" id="2202">
                <div class="framenr">2202</div>
                <div class="kanji">柴</div>
                <div class="keyword" style="display: none">brushwood</div>
            </div>

            <div class="divTableCell" id="2203">
                <div class="framenr">2203</div>
                <div class="kanji">些</div>
                <div class="keyword" style="display: none">whit</div>
            </div>

            <div class="divTableCell" id="2204">
                <div class="framenr">2204</div>
                <div class="kanji">砦</div>
                <div class="keyword" style="display: none">fort</div>
            </div>

            <div class="divTableCell" id="2205">
                <div class="framenr">2205</div>
                <div class="kanji">髭</div>
                <div class="keyword" style="display: none">beard</div>
            </div>

            <div class="divTableCell" id="2206">
                <div class="framenr">2206</div>
                <div class="kanji">禽</div>
                <div class="keyword" style="display: none">fowl</div>
            </div>

            <div class="divTableCell" id="2207">
                <div class="framenr">2207</div>
                <div class="kanji">檎</div>
                <div class="keyword" style="display: none">apple</div>
            </div>

            <div class="divTableCell" id="2208">
                <div class="framenr">2208</div>
                <div class="kanji">憐</div>
                <div class="keyword" style="display: none">sympathize with</div>
            </div>

            <div class="divTableCell" id="2209">
                <div class="framenr">2209</div>
                <div class="kanji">燐</div>
                <div class="keyword" style="display: none">phosphorus</div>
            </div>

            <div class="divTableCell" id="2210">
                <div class="framenr">2210</div>
                <div class="kanji">麟</div>
                <div class="keyword" style="display: none">camelopard</div>
            </div>

            <div class="divTableCell" id="2211">
                <div class="framenr">2211</div>
                <div class="kanji">鱗</div>
                <div class="keyword" style="display: none">scaled</div>
            </div>

            <div class="divTableCell" id="2212">
                <div class="framenr">2212</div>
                <div class="kanji">奄</div>
                <div class="keyword" style="display: none">encompassing</div>
            </div>

            <div class="divTableCell" id="2213">
                <div class="framenr">2213</div>
                <div class="kanji">庵</div>
                <div class="keyword" style="display: none">hermitage</div>
            </div>

            <div class="divTableCell" id="2214">
                <div class="framenr">2214</div>
                <div class="kanji">掩</div>
                <div class="keyword" style="display: none">shrouded</div>
            </div>

            <div class="divTableCell" id="2215">
                <div class="framenr">2215</div>
                <div class="kanji">悛</div>
                <div class="keyword" style="display: none">make amends</div>
            </div>

            <div class="divTableCell" id="2216">
                <div class="framenr">2216</div>
                <div class="kanji">駿</div>
                <div class="keyword" style="display: none">steed</div>
            </div>

            <div class="divTableCell" id="2217">
                <div class="framenr">2217</div>
                <div class="kanji">峻</div>
                <div class="keyword" style="display: none">steep</div>
            </div>

            <div class="divTableCell" id="2218">
                <div class="framenr">2218</div>
                <div class="kanji">竣</div>
                <div class="keyword" style="display: none">complete a job</div>
            </div>

            <div class="divTableCell" id="2219">
                <div class="framenr">2219</div>
                <div class="kanji">犀</div>
                <div class="keyword" style="display: none">rhinoceros</div>
            </div>

            <div class="divTableCell" id="2220">
                <div class="framenr">2220</div>
                <div class="kanji">皐</div>
                <div class="keyword" style="display: none">lunar month</div>
            </div>

            <div class="divTableCell" id="2221">
                <div class="framenr">2221</div>
                <div class="kanji">畷</div>
                <div class="keyword" style="display: none">rice-field footpath</div>
            </div>

            <div class="divTableCell" id="2222">
                <div class="framenr">2222</div>
                <div class="kanji">綴</div>
                <div class="keyword" style="display: none">mend(compose/spell)</div>
            </div>

            <div class="divTableCell" id="2223">
                <div class="framenr">2223</div>
                <div class="kanji">鎧</div>
                <div class="keyword" style="display: none">suit of armor</div>
            </div>

            <div class="divTableCell" id="2224">
                <div class="framenr">2224</div>
                <div class="kanji">凱</div>
                <div class="keyword" style="display: none">triumph</div>
            </div>

            <div class="divTableCell" id="2225">
                <div class="framenr">2225</div>
                <div class="kanji">呑</div>
                <div class="keyword" style="display: none">quaff</div>
            </div>

            <div class="divTableCell" id="2226">
                <div class="framenr">2226</div>
                <div class="kanji">韮</div>
                <div class="keyword" style="display: none">leek</div>
            </div>

            <div class="divTableCell" id="2227">
                <div class="framenr">2227</div>
                <div class="kanji">籤</div>
                <div class="keyword" style="display: none">lottery</div>
            </div>

            <div class="divTableCell" id="2228">
                <div class="framenr">2228</div>
                <div class="kanji">懺</div>
                <div class="keyword" style="display: none">penitential</div>
            </div>

            <div class="divTableCell" id="2229">
                <div class="framenr">2229</div>
                <div class="kanji">芻</div>
                <div class="keyword" style="display: none">hay</div>
            </div>

            <div class="divTableCell" id="2230">
                <div class="framenr">2230</div>
                <div class="kanji">雛</div>
                <div class="keyword" style="display: none">chick</div>
            </div>

            <div class="divTableCell" id="2231">
                <div class="framenr">2231</div>
                <div class="kanji">趨</div>
                <div class="keyword" style="display: none">scurry</div>
            </div>

            <div class="divTableCell" id="2232">
                <div class="framenr">2232</div>
                <div class="kanji">尤</div>
                <div class="keyword" style="display: none">understandably</div>
            </div>

            <div class="divTableCell" id="2233">
                <div class="framenr">2233</div>
                <div class="kanji">厖</div>
                <div class="keyword" style="display: none">immense</div>
            </div>

            <div class="divTableCell" id="2234">
                <div class="framenr">2234</div>
                <div class="kanji">或</div>
                <div class="keyword" style="display: none">a (a certain)</div>
            </div>

            <div class="divTableCell" id="2235">
                <div class="framenr">2235</div>
                <div class="kanji">兎</div>
                <div class="keyword" style="display: none">rabbit</div>
            </div>

            <div class="divTableCell" id="2236">
                <div class="framenr">2236</div>
                <div class="kanji">也</div>
                <div class="keyword" style="display: none">est (to be)</div>
            </div>

            <div class="divTableCell" id="2237">
                <div class="framenr">2237</div>
                <div class="kanji">巴</div>
                <div class="keyword" style="display: none">comma-design</div>
            </div>

            <div class="divTableCell" id="2238">
                <div class="framenr">2238</div>
                <div class="kanji">疋</div>
                <div class="keyword" style="display: none">critters</div>
            </div>

            <div class="divTableCell" id="2239">
                <div class="framenr">2239</div>
                <div class="kanji">菫</div>
                <div class="keyword" style="display: none">violet</div>
            </div>

            <div class="divTableCell" id="2240">
                <div class="framenr">2240</div>
                <div class="kanji">曼</div>
                <div class="keyword" style="display: none">mandala</div>
            </div>

            <div class="divTableCell" id="2241">
                <div class="framenr">2241</div>
                <div class="kanji">云</div>
                <div class="keyword" style="display: none">quote</div>
            </div>

            <div class="divTableCell" id="2242">
                <div class="framenr">2242</div>
                <div class="kanji">莫</div>
                <div class="keyword" style="display: none">shalt</div>
            </div>

            <div class="divTableCell" id="2243">
                <div class="framenr">2243</div>
                <div class="kanji">而</div>
                <div class="keyword" style="display: none">and then</div>
            </div>

            <div class="divTableCell" id="2244">
                <div class="framenr">2244</div>
                <div class="kanji">倭</div>
                <div class="keyword" style="display: none">Yamato</div>
            </div>

            <div class="divTableCell" id="2245">
                <div class="framenr">2245</div>
                <div class="kanji">侠</div>
                <div class="keyword" style="display: none">chivalry</div>
            </div>

            <div class="divTableCell" id="2246">
                <div class="framenr">2246</div>
                <div class="kanji">倦</div>
                <div class="keyword" style="display: none">fed up</div>
            </div>

            <div class="divTableCell" id="2247">
                <div class="framenr">2247</div>
                <div class="kanji">俄</div>
                <div class="keyword" style="display: none">abrupt</div>
            </div>

            <div class="divTableCell" id="2248">
                <div class="framenr">2248</div>
                <div class="kanji">佃</div>
                <div class="keyword" style="display: none">work a field</div>
            </div>

            <div class="divTableCell" id="2249">
                <div class="framenr">2249</div>
                <div class="kanji">仔</div>
                <div class="keyword" style="display: none">animal offspring</div>
            </div>

            <div class="divTableCell" id="2250">
                <div class="framenr">2250</div>
                <div class="kanji">仇</div>
                <div class="keyword" style="display: none">foe</div>
            </div>

            <div class="divTableCell" id="2251">
                <div class="framenr">2251</div>
                <div class="kanji">伽</div>
                <div class="keyword" style="display: none">look after</div>
            </div>

            <div class="divTableCell" id="2252">
                <div class="framenr">2252</div>
                <div class="kanji">儲</div>
                <div class="keyword" style="display: none">make a profit, be profitable</div>
            </div>

            <div class="divTableCell" id="2253">
                <div class="framenr">2253</div>
                <div class="kanji">僑</div>
                <div class="keyword" style="display: none">emigrant</div>
            </div>

            <div class="divTableCell" id="2254">
                <div class="framenr">2254</div>
                <div class="kanji">倶</div>
                <div class="keyword" style="display: none">mate,both</div>
            </div>

            <div class="divTableCell" id="2255">
                <div class="framenr">2255</div>
                <div class="kanji">侃</div>
                <div class="keyword" style="display: none">forthright</div>
            </div>

            <div class="divTableCell" id="2256">
                <div class="framenr">2256</div>
                <div class="kanji">偲</div>
                <div class="keyword" style="display: none">memorial</div>
            </div>

            <div class="divTableCell" id="2257">
                <div class="framenr">2257</div>
                <div class="kanji">侭</div>
                <div class="keyword" style="display: none">as is</div>
            </div>

            <div class="divTableCell" id="2258">
                <div class="framenr">2258</div>
                <div class="kanji">脩</div>
                <div class="keyword" style="display: none">dried meat</div>
            </div>

            <div class="divTableCell" id="2259">
                <div class="framenr">2259</div>
                <div class="kanji">倅</div>
                <div class="keyword" style="display: none">my son</div>
            </div>

            <div class="divTableCell" id="2260">
                <div class="framenr">2260</div>
                <div class="kanji">做</div>
                <div class="keyword" style="display: none">make do(alt)</div>
            </div>

            <div class="divTableCell" id="2261">
                <div class="framenr">2261</div>
                <div class="kanji">冴</div>
                <div class="keyword" style="display: none">sharp</div>
            </div>

            <div class="divTableCell" id="2262">
                <div class="framenr">2262</div>
                <div class="kanji">凋</div>
                <div class="keyword" style="display: none">wilt</div>
            </div>

            <div class="divTableCell" id="2263">
                <div class="framenr">2263</div>
                <div class="kanji">凌</div>
                <div class="keyword" style="display: none">pull through</div>
            </div>

            <div class="divTableCell" id="2264">
                <div class="framenr">2264</div>
                <div class="kanji">凛</div>
                <div class="keyword" style="display: none">stately</div>
            </div>

            <div class="divTableCell" id="2265">
                <div class="framenr">2265</div>
                <div class="kanji">凧</div>
                <div class="keyword" style="display: none">kite</div>
            </div>

            <div class="divTableCell" id="2266">
                <div class="framenr">2266</div>
                <div class="kanji">凪</div>
                <div class="keyword" style="display: none">lull</div>
            </div>

            <div class="divTableCell" id="2267">
                <div class="framenr">2267</div>
                <div class="kanji">夙</div>
                <div class="keyword" style="display: none">earlybird</div>
            </div>

            <div class="divTableCell" id="20010">
                <div class="framenr">20010</div>
                <div class="kanji">个</div>
                <div class="keyword" style="display: none">counter for articles;  individua</div>
            </div>

            <div class="divTableCell" id="20022">
                <div class="framenr">20022</div>
                <div class="kanji">丶</div>
                <div class="keyword" style="display: none">dot, tick or dot radical</div>
            </div>

            <div class="divTableCell" id="20031">
                <div class="framenr">20031</div>
                <div class="kanji">丿</div>
                <div class="keyword" style="display: none">katakana no radical</div>
            </div>

            <div class="divTableCell" id="20034">
                <div class="framenr">20034</div>
                <div class="kanji">乂</div>
                <div class="keyword" style="display: none">mow; cut grass; subdue</div>
            </div>

            <div class="divTableCell" id="20101">
                <div class="framenr">20101</div>
                <div class="kanji">亅</div>
                <div class="keyword" style="display: none">feathered stick; barb radical</div>
            </div>

            <div class="divTableCell" id="31840">
                <div class="framenr">31840</div>
                <div class="kanji">籠</div>
                <div class="keyword" style="display: none">cage (Joyo version)</div>
            </div>
        </div>
    </div>
"""

# Parse the HTML
root = ET.fromstring(html)

# Extract the data
data = []
for cell in root.find('.//div[@class="divTableBody"]'):
    id = cell.attrib['id']
    kanji = cell.find('.//div[@class="kanji"]').text
    keyword = cell.find('.//div[@class="keyword"]').text
    data.append({ 'id': id, 'kanji': kanji, 'keyword': keyword })

# Convert the data to a JSON string
data_json = json.dumps(data, ensure_ascii=False)

# Write the data to a JavaScript file
with open('result.js', 'w', encoding='utf8') as f:
    f.write('var data = ' + data_json + ';')