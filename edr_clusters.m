%file_path = "A:\University of Cincinnati\theses\Codes\Phase6_Cluster_Extraction\Results\results2.csv";

function [a, dist] = edr_clusters(c1, c2, node1,node2)
    s1 = c1;
    s2 = c2;

    c1 = normalize(c1, 'norm', 1);
    c2 = normalize(c2, 'norm', 1);

    [c1, c1order] = sort(c1, 'descend');
    [c2, c2order] = sort(c2, 'descend');

    node1 = node1(c1order);
    node2 = node2(c2order);

    s1 = s1(c1order);
    s2 = s2(c2order);

    %disp(node1);
    %disp(node2);

    %disp(s1);
    %disp(s2);

    [dist, ix, iy] = edr(c1, c2, 0.1);
    %disp([ix iy]);
    res = [];
    a = [];

    for i = 1: length(iy)     
        %res = [ix(i) iy(i) node1(ix(i)) node2(iy(i)) s1(ix(i)) s2(iy(i)) (s1(ix(i)) - s2(iy(i))).^2];
		res = [ix(i) iy(i) node1(ix(i)) node2(iy(i)) c1(ix(i)) c2(iy(i)) (c1(ix(i)) - c2(iy(i))).^2];
        a = [a ; res]; 
    end
end
