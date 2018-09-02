<?php
require __DIR__.'/vendor/autoload.php';

$additional_head = "
    <style>
    :target:before {
        content:\"\";
        display:block;
        height:90px; /* fixed header height*/
        margin:-90px 0 0; /* negative fixed header height */
    }
    </style>
    <meta property='og:type' content='website'>
    <meta property='og:site_name' content='neowiki'>
";

class MDParser implements Mni\FrontYAML\Markdown\MarkdownParser {
    public function __construct() {
        $this->mdparser = new Michelf\MarkdownExtra();
        $this->mdparser->header_id_func = function ($header) {
            return preg_replace('/[^a-z0-9]/', '-', strtolower($header));
        };
    }

    public function parse($markdown) {
        return $this->mdparser->transform($markdown);
    }
}

$parser = new Mni\FrontYAML\Parser(null, new MDParser());


if (!isset($_GET["article"]) || !file_exists("articles/{$_GET['article']}.md")) {

    $title = "neowiki";
    $additional_head .= "
    <meta property='og:title' content='$title'>
    <meta property='og:url' content='https://khuxkm.tilde.team{$_SERVER['REQUEST_URI']}'>
    <meta property='og:description' content='a wiki for neocities'>
    ";
    include __DIR__.'/header.php';
    // render wiki index ?>

    <h1>neowiki</h1>

    <p>welcome to neowiki!</p>

    <p>if you want to contribute, check out the
        <a href="https://github.com/MineRobber9000/neowiki">source</a> and open a PR!
    </p>

    <hr>
    <h3>articles:</h3>

    <?php
    foreach (glob("articles/*.md") as $article) {
        $yaml = $parser->parse(file_get_contents($article))->getYAML();
        if (!$yaml["published"]) continue; ?>
        <a href="?article=<?=basename($article, ".md")?>"><?=$yaml["title"]?></a><br>
    <?php }

} else {

    $pg = $parser->parse(file_get_contents("articles/{$_GET["article"]}.md"));
    $yml = $pg->getYAML();
    $title = $yml['title'] . " | neowiki";
    $description = $yml['description'] ?? "neowiki article {$yml['title']}";
    $additional_head .= "
    <meta property='og:title' content='$title'>
    <meta property='og:url' content='https://khuxkm.tilde.team{$_SERVER['REQUEST_URI']}'>
    <meta property='og:description' content='$description'>
    ";
    include __DIR__.'/header.php';
    // show a single article ?>

    <a href=".">&lt; main article</a>

    <hr>
        <?=$pg->getContent()?>
    <hr>
    <a href="https://github.com/MineRobber9000/neowiki/blob/master/articles/<?=$_GET["article"]?>.md">
        <i class="fa fa-edit"></i> source
    </a>

<?php }

include __DIR__.'/footer.php';
