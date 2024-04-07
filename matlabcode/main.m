


%% 
% Pelican Optimization Algorithm: A New Bio-Inspired Optimization Approach
% MDPI_Applied Science
% Pavel Trojovský1 and Mohammad Dehghani
% Department of Mathematics, Faculty of Science, University of Hradec Králové, 50003 Hradec Králové, Czech Republic

% " Optimizer"
%%
clc
clear
close all
%%

%%
Fun_name='F1'; % number of test functions: 'F1' to 'F23'

SearchAgents=30;                      % number of Pelicans (population members) 
Max_iterations=1000;                  % maximum number of iteration
[lowerbound,upperbound,dimension,fitness]=fun_info(Fun_name); % Object function information
[Best_score,Best_pos,POA_curve]=POA(SearchAgents,Max_iterations,lowerbound,upperbound,dimension,fitness);  % Calculating the solution of the given problem using POA 

%%

display(['The best solution obtained by POA for ' [num2str(Fun_name)],'  is : ', num2str(Best_pos)]);
display(['The best optimal value of the objective funciton found by POA  for ' [num2str(Fun_name)],'  is : ', num2str(Best_score)]);


        