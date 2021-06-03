// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================

`timescale 1 ns / 1 ps

`define TV_OUT_outStream_TDATA "../tv/rtldatafile/rtl.image_inverter_BLIp.autotvout_outStream_V_data_V.dat"
`define EGRESS_STATUS_outStream_TDATA "../tv/stream_size/stream_egress_status_outStream_V_data_V.dat"
`define TV_OUT_outStream_TKEEP "../tv/rtldatafile/rtl.image_inverter_BLIp.autotvout_outStream_V_keep_V.dat"
`define EGRESS_STATUS_outStream_TKEEP "../tv/stream_size/stream_egress_status_outStream_V_keep_V.dat"
`define TV_OUT_outStream_TSTRB "../tv/rtldatafile/rtl.image_inverter_BLIp.autotvout_outStream_V_strb_V.dat"
`define EGRESS_STATUS_outStream_TSTRB "../tv/stream_size/stream_egress_status_outStream_V_strb_V.dat"
`define TV_OUT_outStream_TLAST "../tv/rtldatafile/rtl.image_inverter_BLIp.autotvout_outStream_V_last_V.dat"
`define EGRESS_STATUS_outStream_TLAST "../tv/stream_size/stream_egress_status_outStream_V_last_V.dat"

`define AUTOTB_TRANSACTION_NUM 1

module AESL_axi_s_outStream (
    input clk,
    input reset,
    input [8 - 1:0] TRAN_outStream_TDATA,
    input TRAN_outStream_TKEEP,
    input TRAN_outStream_TSTRB,
    input TRAN_outStream_TLAST,
    input TRAN_outStream_TVALID,
    output TRAN_outStream_TREADY,
    input ready,
    input done,
    output [31:0] transaction);

    wire TRAN_outStream_TVALID_temp;
    wire outStream_TDATA_full;
    wire outStream_TDATA_empty;
    reg outStream_TDATA_write_en;
    reg [8 - 1:0] outStream_TDATA_write_data;
    reg outStream_TDATA_read_en;
    wire [8 - 1:0] outStream_TDATA_read_data;
    
    fifo #(1, 8) fifo_outStream_TDATA (
        .reset(1'b0),
        .write_clock(clk),
        .write_en(outStream_TDATA_write_en),
        .write_data(outStream_TDATA_write_data),
        .read_clock(clk),
        .read_en(outStream_TDATA_read_en),
        .read_data(outStream_TDATA_read_data),
        .full(outStream_TDATA_full),
        .empty(outStream_TDATA_empty));
    
    always @ (*) begin
        outStream_TDATA_write_en <= TRAN_outStream_TVALID;
        outStream_TDATA_write_data <= TRAN_outStream_TDATA;
        outStream_TDATA_read_en <= 0;
    end
    wire outStream_TKEEP_full;
    wire outStream_TKEEP_empty;
    reg outStream_TKEEP_write_en;
    reg [1 - 1:0] outStream_TKEEP_write_data;
    reg outStream_TKEEP_read_en;
    wire [1 - 1:0] outStream_TKEEP_read_data;
    
    fifo #(1, 1) fifo_outStream_TKEEP (
        .reset(1'b0),
        .write_clock(clk),
        .write_en(outStream_TKEEP_write_en),
        .write_data(outStream_TKEEP_write_data),
        .read_clock(clk),
        .read_en(outStream_TKEEP_read_en),
        .read_data(outStream_TKEEP_read_data),
        .full(outStream_TKEEP_full),
        .empty(outStream_TKEEP_empty));
    
    always @ (*) begin
        outStream_TKEEP_write_en <= TRAN_outStream_TVALID;
        outStream_TKEEP_write_data <= TRAN_outStream_TKEEP;
        outStream_TKEEP_read_en <= 0;
    end
    wire outStream_TSTRB_full;
    wire outStream_TSTRB_empty;
    reg outStream_TSTRB_write_en;
    reg [1 - 1:0] outStream_TSTRB_write_data;
    reg outStream_TSTRB_read_en;
    wire [1 - 1:0] outStream_TSTRB_read_data;
    
    fifo #(1, 1) fifo_outStream_TSTRB (
        .reset(1'b0),
        .write_clock(clk),
        .write_en(outStream_TSTRB_write_en),
        .write_data(outStream_TSTRB_write_data),
        .read_clock(clk),
        .read_en(outStream_TSTRB_read_en),
        .read_data(outStream_TSTRB_read_data),
        .full(outStream_TSTRB_full),
        .empty(outStream_TSTRB_empty));
    
    always @ (*) begin
        outStream_TSTRB_write_en <= TRAN_outStream_TVALID;
        outStream_TSTRB_write_data <= TRAN_outStream_TSTRB;
        outStream_TSTRB_read_en <= 0;
    end
    wire outStream_TLAST_full;
    wire outStream_TLAST_empty;
    reg outStream_TLAST_write_en;
    reg [1 - 1:0] outStream_TLAST_write_data;
    reg outStream_TLAST_read_en;
    wire [1 - 1:0] outStream_TLAST_read_data;
    
    fifo #(1, 1) fifo_outStream_TLAST (
        .reset(1'b0),
        .write_clock(clk),
        .write_en(outStream_TLAST_write_en),
        .write_data(outStream_TLAST_write_data),
        .read_clock(clk),
        .read_en(outStream_TLAST_read_en),
        .read_data(outStream_TLAST_read_data),
        .full(outStream_TLAST_full),
        .empty(outStream_TLAST_empty));
    
    always @ (*) begin
        outStream_TLAST_write_en <= TRAN_outStream_TVALID;
        outStream_TLAST_write_data <= TRAN_outStream_TLAST;
        outStream_TLAST_read_en <= 0;
    end
    assign TRAN_outStream_TVALID = TRAN_outStream_TVALID_temp;

    
    assign TRAN_outStream_TREADY = ~(outStream_TDATA_full || outStream_TKEEP_full || outStream_TSTRB_full || outStream_TLAST_full);
    
    function is_blank_char(input [7:0] in_char);
        if (in_char == " " || in_char == "\011" || in_char == "\012" || in_char == "\015") begin
            is_blank_char = 1;
        end else begin
            is_blank_char = 0;
        end
    endfunction
    
    function [151:0] read_token(input integer fp);
        integer ret;
        begin
            read_token = "";
                    ret = 0;
                    ret = $fscanf(fp,"%s",read_token);
        end
    endfunction
    
    function [151:0] rm_0x(input [151:0] token);
        reg [151:0] token_tmp;
        integer i;
        begin
            token_tmp = "";
            for (i = 0; token[15:0] != "0x"; token = token >> 8) begin
                token_tmp = (token[7:0] << (8 * i)) | token_tmp;
                i = i + 1;
            end
            rm_0x = token_tmp;
        end
    endfunction
    
    reg done_1;
    
    always @ (posedge clk or reset) begin
        if (~reset) begin
            done_1 <= 0;
        end else begin
            done_1 <= done;
        end
    end
    
    reg [31:0] transaction_save_outStream_TDATA;
    
    assign transaction = transaction_save_outStream_TDATA;
    
    initial begin : AXI_stream_receiver_outStream_TDATA
        integer fp;
        reg [8 - 1:0] data;
        reg [8 * 5:1] str;
        
        transaction_save_outStream_TDATA = 0;
        fifo_outStream_TDATA.clear();
        wait (reset === 1);
        forever begin
            @ (negedge clk);
            if (done_1 == 1) begin
                fp = $fopen(`TV_OUT_outStream_TDATA, "a");
                if (fp == 0) begin // Failed to open file
                    $display("ERROR: Failed to open file \"%s\"!", `TV_OUT_outStream_TDATA);
                    $finish;
                end
                $fdisplay(fp, "[[transaction]] %d", transaction_save_outStream_TDATA);
                while (~fifo_outStream_TDATA.empty) begin
                    fifo_outStream_TDATA.pop(data);
                    $fdisplay(fp, "0x%x", data);
                end
                $fdisplay(fp, "[[/transaction]]");
                transaction_save_outStream_TDATA = transaction_save_outStream_TDATA + 1;
                fifo_outStream_TDATA.clear();
                $fclose(fp);
            end
        end
    end
    
    reg [31:0] transaction_save_outStream_TKEEP;
    
    initial begin : AXI_stream_receiver_outStream_TKEEP
        integer fp;
        reg [1 - 1:0] data;
        reg [8 * 5:1] str;
        
        transaction_save_outStream_TKEEP = 0;
        fifo_outStream_TKEEP.clear();
        wait (reset === 1);
        forever begin
            @ (negedge clk);
            if (done_1 == 1) begin
                fp = $fopen(`TV_OUT_outStream_TKEEP, "a");
                if (fp == 0) begin // Failed to open file
                    $display("ERROR: Failed to open file \"%s\"!", `TV_OUT_outStream_TKEEP);
                    $finish;
                end
                $fdisplay(fp, "[[transaction]] %d", transaction_save_outStream_TKEEP);
                while (~fifo_outStream_TKEEP.empty) begin
                    fifo_outStream_TKEEP.pop(data);
                    $fdisplay(fp, "0x%x", data);
                end
                $fdisplay(fp, "[[/transaction]]");
                transaction_save_outStream_TKEEP = transaction_save_outStream_TKEEP + 1;
                fifo_outStream_TKEEP.clear();
                $fclose(fp);
            end
        end
    end
    
    reg [31:0] transaction_save_outStream_TSTRB;
    
    initial begin : AXI_stream_receiver_outStream_TSTRB
        integer fp;
        reg [1 - 1:0] data;
        reg [8 * 5:1] str;
        
        transaction_save_outStream_TSTRB = 0;
        fifo_outStream_TSTRB.clear();
        wait (reset === 1);
        forever begin
            @ (negedge clk);
            if (done_1 == 1) begin
                fp = $fopen(`TV_OUT_outStream_TSTRB, "a");
                if (fp == 0) begin // Failed to open file
                    $display("ERROR: Failed to open file \"%s\"!", `TV_OUT_outStream_TSTRB);
                    $finish;
                end
                $fdisplay(fp, "[[transaction]] %d", transaction_save_outStream_TSTRB);
                while (~fifo_outStream_TSTRB.empty) begin
                    fifo_outStream_TSTRB.pop(data);
                    $fdisplay(fp, "0x%x", data);
                end
                $fdisplay(fp, "[[/transaction]]");
                transaction_save_outStream_TSTRB = transaction_save_outStream_TSTRB + 1;
                fifo_outStream_TSTRB.clear();
                $fclose(fp);
            end
        end
    end
    
    reg [31:0] transaction_save_outStream_TLAST;
    
    initial begin : AXI_stream_receiver_outStream_TLAST
        integer fp;
        reg [1 - 1:0] data;
        reg [8 * 5:1] str;
        
        transaction_save_outStream_TLAST = 0;
        fifo_outStream_TLAST.clear();
        wait (reset === 1);
        forever begin
            @ (negedge clk);
            if (done_1 == 1) begin
                fp = $fopen(`TV_OUT_outStream_TLAST, "a");
                if (fp == 0) begin // Failed to open file
                    $display("ERROR: Failed to open file \"%s\"!", `TV_OUT_outStream_TLAST);
                    $finish;
                end
                $fdisplay(fp, "[[transaction]] %d", transaction_save_outStream_TLAST);
                while (~fifo_outStream_TLAST.empty) begin
                    fifo_outStream_TLAST.pop(data);
                    $fdisplay(fp, "0x%x", data);
                end
                $fdisplay(fp, "[[/transaction]]");
                transaction_save_outStream_TLAST = transaction_save_outStream_TLAST + 1;
                fifo_outStream_TLAST.clear();
                $fclose(fp);
            end
        end
    end

endmodule
