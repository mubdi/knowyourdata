"""
Template for HTML version of Data Summary
"""

kyd_htmltemplate = """
<style>

.kydbox {{
  border-style: solid;
  border-color: #CCCCCC;
  border-width: 2px;
  margin: 10px;
  padding: 5px;
  font-family: sans-serif;
  font-size: 10pt;
}}

.kydfloatboxleft {{
  margin: 5px;
  padding-left: 10px;
  float: left;
  border-right-width: 2px;
  border-right-style: solid;
  border-right-color: #CCCCCC;
  padding-right: 15px;
  margin-right: 15px;
}}

.kydfloatboxright {{
  margin: 5px;
  padding-right: 10px;
  float: right;
}}

.kydsubtitle {{
  font-size: 10pt;
  font-weight: bold;
  margin-top: 5px;
  margin-bottom: 5px;
}}

.kydpropertylabel {{
  font-weight: bold;
}}

td.kydpropertylabel {{
  text-align: right;
}}

table.kydbasic_stats,
table.kydarray_structure {{
  padding-top: 0px;
}}

table.kydbasic_stats td,
table.kydarray_structure td {{
  padding: 3px 10px 3px 10px;
}}

.kydbottomborder {{
  border-bottom-width:2px;
  border-bottom-style:solid;
  border-bottom-color:#CCCCCC;
}}

</style>

<div class="kydbox" , style="float:left">

  <div class="kydfloatboxleft">
    <div class="kydsubtitle">Basic Statistics</div>

    <span class='kydpropertylabel'>Mean:</span>
    {kyd_class.mean:.{kyd_class.precision}}
    &nbsp;&nbsp;&nbsp;&nbsp;
    <span class='kydpropertylabel'>Std Dev:</span>
    {kyd_class.std:.{kyd_class.precision}}

    <table class="kydbasic_stats">
      <tr>
        <td class='kydpropertylabel'>Min:</td>
        <td>{kyd_class.min:.{kyd_class.precision}}</td>
        <td class='kydpropertylabel'>-99% CI:</td>
        <td>{kyd_class.ci_99[0]:.{kyd_class.precision}}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>1Q:</td>
        <td>{kyd_class.firstquartile:.{kyd_class.precision}}</td>
        <td class='kydpropertylabel'>-95% CI:</td>
        <td>{kyd_class.ci_95[0]:.{kyd_class.precision}}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Median:</td>
        <td>{kyd_class.median:.{kyd_class.precision}}</td>
        <td class='kydpropertylabel'>-68% CI:</td>
        <td>{kyd_class.ci_68[0]:.{kyd_class.precision}}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>3Q:</td>
        <td>{kyd_class.thirdquartile:.{kyd_class.precision}}</td>
        <td class='kydpropertylabel'>+68% CI:</td>
        <td>{kyd_class.ci_68[1]:.{kyd_class.precision}}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Max:</td>
        <td>{kyd_class.max:.{kyd_class.precision}}</td>
        <td class='kydpropertylabel'>+95% CI:</td>
        <td>{kyd_class.ci_95[1]:.{kyd_class.precision}}</td>
      </tr>
      <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td class='kydpropertylabel'>+99% CI:</td>
        <td>{kyd_class.ci_99[1]:.{kyd_class.precision}}</td>
      </tr>

    </table>
  </div>

  <div class="kydfloatboxright">
    <div class="kydsubtitle">Array Structure</div>
    <table class="kydarray_structure">
      <tr>
        <td class='kydpropertylabel'>Number of Dimensions:</td>
        <td>{kyd_class.ndim}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Shape of Dimensions:</td>
        <td>{kyd_class.shape}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Array Data Type:</td>
        <td>{kyd_class.dtype}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Memory Size:</td>
        <td>{kyd_class.human_memsize}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Number of NaN:</td>
        <td>{kyd_class.num_nan}</td>
      </tr>
      <tr>
        <td class='kydpropertylabel'>Number of Inf:</td>
        <td>{kyd_class.num_inf}</td>
      </tr>

    </table>
  </div>

</div>
"""
