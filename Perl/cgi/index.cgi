#!/user/bin/env perl
use Modern::Perl;
use Mojolicious::Lite;

get '/' => sub {
    my $self = shift;
    $self->render ( 'homepage' );
};
app->start;

__DATA__
@@ homepage.html.ep
index.cgi works!!